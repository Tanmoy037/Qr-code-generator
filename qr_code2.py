import qrcode
from PIL import Image
qr= qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=4)
var1 = str(input("Enter the object you want to make QR code : "))
qr.add_data(var1)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
var2 = str(input("Enter the name you want to save for the QR code : "))
img.save(var2)
