from email.message import EmailMessage
import smtplib,os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_mail(message, filename):
	img_data = open(filename, 'rb').read()
	msg = MIMEMultipart()
	msg['Subject'] = 'subject'
	msg['From'] = 'niharikachosweet@gmail.com'
	msg['To'] = 'matcha72@gmail.com'
	msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % ("Check this", filename), 'html')  
	msg.attach(msgText)   # Added, and edited the previous line
	fp = open(filename, 'rb')                                                    
	img = MIMEImage(fp.read())
	fp.close()
	img.add_header('Content-ID', '<{}>'.format(filename))
	msg.attach(img)	
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(msg['From'], 'hindijanu')
	s.sendmail(msg['From'], msg['To'], msg.as_string())
	s.quit()
	
send_mail("Hello")	