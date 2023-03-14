import cv2

from pyzbar.pyzbar import decode

img = cv2.imread('qr.jpg') # read the picture from directory.

info = decode(img) # decode qr code

print(info) # Printing information as list.


