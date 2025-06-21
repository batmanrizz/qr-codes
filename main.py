'''
This is a simple Python code that creates a QR code for eSewa.

It gives you a basic understanding of how QR codes work. It's just as simple as that.

clone this repo

RUN--> python3 -m venv venv

pip install -r requirements.txt


'''

import qrcode

data = (input("Enter your number--> "))
name = input("Enter your name--> ")
rdata = "eSewa_id"

new_dict = {
    rdata:data, 
    "name": name   #You can add custom names bank will read only number
            
            
            
            }

img = qrcode.make(f'{new_dict}')


type(img)  # qrcode.image.pil.PilImage
img.save("esewa.png")

