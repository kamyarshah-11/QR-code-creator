import os
import tkinter as tk
from tkinter import filedialog, messagebox

from base import qr_creator_text


class QRWindow:
    COLORS = {
        "bg": "#100202",
        "main": "#88038B",
        "panel": "#5E075F",
        "accent": "#D946EF",
        "accent_hover": "#E879F9",
        "text": "#FFFFFF",
        "muted": "#E9D5FF",
        "input_bg": "#210A21",
        "border": "#A21CAF",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Kamyar QR Code Creator")
        self.root.geometry("900x650")
        self.root.iconbitmap("test.ico")
        self.root.configure(bg=self.COLORS["bg"])
        self.root.resizable(False, False)

        self.current_file = None
        self.create_ui()

    def create_ui(self):
        # Header
        header = tk.Frame(self.root, bg=self.COLORS["bg"])
        header.pack(fill="x", padx=35, pady=(25, 10))

        tk.Label(
            header,
            text="QR CODE",
            font=("Segoe UI", 25, "bold"),
            bg=self.COLORS["bg"],
            fg=self.COLORS["text"],
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Convert your text into a QR Code",
            font=("Segoe UI", 11),
            bg=self.COLORS["bg"],
            fg=self.COLORS["muted"],
        ).pack(anchor="w", pady=(3, 0))

        # Main card
        card = tk.Frame(
            self.root,
            bg=self.COLORS["main"],
            highlightthickness=1,
            highlightbackground=self.COLORS["border"],
        )
        card.pack(fill="both", expand=True, padx=35, pady=15)

        # Text section
        text_section = tk.Frame(card, bg=self.COLORS["main"])
        text_section.pack(fill="both", expand=True, padx=25, pady=22)

        tk.Label(
            text_section,
            text="TEXT / FILE CONTENT",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLORS["main"],
            fg=self.COLORS["text"],
        ).pack(anchor="w")

        self.txt_box = tk.Text(
            text_section,
            height=18,
            font=("Consolas", 11),
            bg=self.COLORS["input_bg"],
            fg=self.COLORS["text"],
            insertbackground=self.COLORS["text"],
            selectbackground=self.COLORS["accent"],
            relief="flat",
            bd=0,
            padx=14,
            pady=14,
            wrap="word",
        )
        self.txt_box.pack(fill="both", expand=True, pady=(8, 15))

        # Bottom controls
        controls = tk.Frame(card, bg=self.COLORS["main"])
        controls.pack(fill="x", padx=25, pady=(0, 22))

        self.file_label = tk.Label(
            controls,
            text="No file selected",
            font=("Segoe UI", 9),
            bg=self.COLORS["main"],
            fg=self.COLORS["muted"],
        )
        self.file_label.pack(side="left")

        button_area = tk.Frame(controls, bg=self.COLORS["main"])
        button_area.pack(side="right")

        self.create_btn = self.make_button(
            button_area,
            "CREATE QR",
            self.create_qr,
            self.COLORS["accent"],
        )
        self.create_btn.pack(side="right", padx=(8, 0))

        self.open_btn = self.make_button(
            button_area,
            "OPEN QR",
            self.open_qr,
            self.COLORS["panel"],
        )
        self.open_btn.pack(side="right", padx=(8, 0))

        self.file_btn = self.make_button(
            button_area,
            "OPEN TXT",
            self.choose_file,
            self.COLORS["panel"],
        )
        self.file_btn.pack(side="right")

    def make_button(self, parent, text, command, bg):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 9, "bold"),
            bg=bg,
            fg=self.COLORS["text"],
            activebackground=self.COLORS["accent_hover"],
            activeforeground=self.COLORS["text"],
            relief="flat",
            bd=0,
            padx=18,
            pady=9,
            cursor="hand2",
        )
        return button

    def choose_file(self):
        path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[
                ("Text files", "*.txt"),
            ],
        )

        if not path:
            return

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = f.read()

            self.txt_box.delete("1.0", tk.END)
            self.txt_box.insert("1.0", data)

            self.current_file = path
            self.file_label.config(text=f"Selected: {os.path.basename(path)}")

        except UnicodeDecodeError:
            messagebox.showerror(
                "Invalid file", "This file could not be read as UTF-8 text."
            )
        except OSError as error:
            messagebox.showerror("Error", str(error))

    def create_qr(self):
        data = self.txt_box.get("1.0", "end-1c").strip()

        if not data:
            messagebox.showwarning(
                "Empty text", "Please enter some text or open a .txt file first."
            )
            return

        try:
            qr_creator_text(data, "image.png")

            messagebox.showinfo("Success", "QR Code created successfully.")

        except Exception as error:
            messagebox.showerror("Error", f"Could not create the QR Code.\n\n{error}")

    def open_qr(self):
        image_path = os.path.abspath("image.png")

        if not os.path.exists(image_path):
            messagebox.showwarning("QR Code not found", "Create a QR Code first.")
            return

        try:
            os.startfile(image_path)
        except OSError as error:
            messagebox.showerror("Error", str(error))


if __name__ == "__main__":
    root = tk.Tk()
    QRWindow(root)
    root.mainloop()
