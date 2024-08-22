#step1: run this in terminal, pip install qrcode[pil]
import qrcode

#data to put in qrcode
data = "https://github.com/soyRex-codes"

#creating qrcode
qr = qrcode.QRCode(
    version = 1, #controls the size of QR from 1 to 40
#########################################################
# QR Code Damage protection:
#1. situations where our QR code is severely damaged but we still want it to work, in such situations we use error protection
#where L  as lowest:7% and H for Highest:30% protection
#but a trade of is more protection so less storage space for data and vice versa
#########################################################     """
    error_correction=qrcode.constants.ERROR_CORRECT_H, #error correction level (L, M, Q, H)
    
    box_size = 10, #set the size of the box in pixesl
    border = 4, #set the border size in pixels
)

#adding data to the qr code
qr.add_data(data) #this add our data to the QRCode
qr.make(fit=True) #fits our data into the QRCode

#creating an image from the QRCode
#we use the make method to create the QRCode and then we use the make_img method to create an image from QRCode
img = qr.make_image(fill='blue', back_color='white')

#saving the image
img.save("qrcode.png")

#######################################################
# NOTE:To find the png file, type dir in the terminal to see the 
# current Directory where file is saved, you should be getting a list, look for qrcoode.png in the list
# , if you see it then it is sucessfully created and is loacted there, acess it from that folder, currently for me it is saved in  C:\Users\rajku
#########################################################





