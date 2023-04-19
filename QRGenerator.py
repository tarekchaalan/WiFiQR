import qrcode
from urllib.parse import quote
import os

# file name
filename = "WiFi QR"

# credentials
ssid = "SSID HERE"
password = "WIFI PASS HERE"

# encode ssid and password
encoded_ssid = quote(ssid)
encoded_password = quote(password)

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = "WIFI:T:WPA;S:{};P:{};;".format(ssid, password)
qr.add_data(data)
qr.make(fit=True)

# Save QR code as png then open it
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename + '.png')
os.startfile(filename + '.png')