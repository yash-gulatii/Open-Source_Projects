import qrcode #import the qrcode module


qr = qrcode.QRCode(
    version = 15,
    box_size = 20,
    border = 10
) #create object of QRCode class

data="https://github.com/arushitrivedi"   #copy the link that has to be directed by the qr-code
qr.add_data(data)   #add the data to qrcode
qr.make(fit=True)   #generate qrcode

img=qr.make_image(fill="black", cack_color="white") #generates image with the given attributes
img.save('qr2.png') #name of the image

