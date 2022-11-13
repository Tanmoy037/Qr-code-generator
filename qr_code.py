import qrcode as qr
var1 = str(input("Enter the object you want to make QR code : "))
img= qr.make(var1)
var2 = str(input("Enter the name you want to save for the QR code : "))
img.save(var2)


