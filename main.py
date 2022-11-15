import pyqrcode


from pyqrcode import QRCode

website = "https://github.com/kyletaylor94"

url = pyqrcode.create(website)

url.svg("myqr.svg", scale = 8)

url.png("myqr.png", scale= 6)