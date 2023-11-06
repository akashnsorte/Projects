import qrcode

features = qrcode.QRCode(version=1,box_size=50,border=2)

features.add_data('https://github.com/akashnsorte')
features.make(fit=True)
generate_image = features.make_image(fill_color="black",back_color="white")
generate_image.save('image2.png')
