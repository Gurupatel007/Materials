import smtplib as s
import imghdr
from email.message import EmailMessage
ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("kevalvasoya20gnu.ac.in","dell153000")
subject = EmailMessage()
subject['Subject'] = "sending image as a content"
subject['From'] = "kevalvasoya20gnu.ac.in" 
subject['To'] = "kevalvasoya744@gmail.com"
with open('h1.jpg', 'rb') as f:
 image_data = f.read()
 image_type = imghdr.what(f.name)
 image_name = f.name
 
subject.add_attachment(image_data, maintype='image', subtype=image_type, 
filename=image_name)
ob.send_message(subject)
ob.quit()