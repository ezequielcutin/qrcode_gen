import qrcode

details = qrcode.QRCode(version=1,box_size=30,border=4)
website = input("enter website link here: ")
details.add_data(website)
details.make(fit=True)
generateQR = details.make_image(fill_color="blue",back_color="yellow")
generateQR.save(website + ".png")



