import qrcode as qr

data = input("Enter the text or URL to generate QR code: ")
img = qr.make(data)
img.save("my_qr.png")
print("It's done successfully")