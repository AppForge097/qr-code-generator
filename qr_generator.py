import qrcode

data = input("Matn yoki havolani kiriting: ")

qr = qrcode.make(data)

qr.save("my_qrcode.png")

print("QR kod muvaffaqiyatli yaratildi!")