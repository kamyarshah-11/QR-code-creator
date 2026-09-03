import tkinter as tk
from base import qr_creator_text


class qr_window:
    COLORS = {"bg": "#100202", "main_frame": "#88038B"}

    def __init__(self, root):
        self.root = root
        self.root.geometry("900x650")
        self.root.title("QR code Creator")
        self.root.configure(bg=self.COLORS["bg"])
        self.root.resizable(False, False)
        self.main_frame = tk.Frame(self.root, bg=self.COLORS["main_frame"])
        self.main_frame.pack(padx=10, pady=10)
        self.text_box()

    def text_box(self):
        self.txt_box = tk.Text(self.main_frame, width=40, height=32)
        self.txt_box.pack(padx=10, pady=10, side="right")
        self.output_img()

    def output_img(self):
        self.qr_image = tk.PhotoImage(file="image.png")

        self.output_image = tk.Label(self.main_frame, image=self.qr_image)
        self.output_image.pack(side="left", padx=10, pady=10)
        self.buttons()

    def buttons(self):
        self.button_frame = tk.Frame(self.main_frame, bg=self.COLORS["main_frame"])
        self.button_frame.pack(side="bottom", pady=10)

        self.convert_btn = tk.Button(
            self.button_frame, text="Convert", command=self.show_qrcode
        )
        self.convert_btn.pack()

    def show_qrcode(self):
        qr_creator_text(self.txt_box.get("1.0", tk.END))

        self.qr_image = tk.PhotoImage(file="image.png")
        self.output_image.config(image=self.qr_image)


if __name__ == "__main__":
    root = tk.Tk()
    qr_window(root)
    root.mainloop()
