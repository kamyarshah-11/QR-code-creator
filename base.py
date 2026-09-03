import qrcode


def qr_creator_text(data):
    qr = qrcode.make(data)
    qr.save("image.png")


def qr_creator_file(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
        qr_creator_text(data)
