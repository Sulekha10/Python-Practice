import qrcode as qr

img = qr.make("https://www.linkedin.com/feed/")
img.save("myLinkedin.png")