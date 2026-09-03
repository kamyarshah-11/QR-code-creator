import qrcode


def qr_creator_text(data, output_path="image.png"):
    qr = qrcode.make(data)
    qr.save(output_path)
    return output_path


def qr_creator_file(path, output_path="image.png"):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()

    return qr_creator_text(data, output_path)
