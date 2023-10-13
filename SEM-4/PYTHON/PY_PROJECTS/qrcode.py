import qrcode

data = "https://www.linkedin.com/in/guru-patel-42423b219"
img = qrcode.make(data)
img.save("GuruPatel1.png")