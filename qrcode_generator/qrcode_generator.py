import qrcode

data = input("Enter some text or URL: ").strip()
filename = input("Enter the file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

image.save(rf"E:\Programing files\Python\Project1\qrcode_generator\qr_images\{filename}.png")

print(f"QR code saved as {filename}.png")