from flask import Flask, render_template, request
from werkzeug import secure_filename
import requests
import json
from email.message import EmailMessage
import smtplib

from email.message import EmailMessage
import smtplib,os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_mail(message, filename):
	img_data = open(filename, 'rb').read()
	msg = MIMEMultipart()
	msg['Subject'] = "Your baby is "+message
	msg['From'] = 'niharikachosweet@gmail.com'
	msg['To'] = 'matcha72@gmail.com'
	msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % ("Your baby is "+message, filename), 'html')  
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



url = "https://firstclassification.cognitiveservices.azure.com/customvision/v3.0/Prediction/f7a8c798-b932-4a9d-bfe8-74e4acc3150b/classify/iterations/Iteration1/image"

url1 = "https://centralindia.api.cognitive.microsoft.com/vision/v2.0/analyze?visualFeatures=Objects&language=en"

headers = {
    'prediction-key': "f725326e539d48adaacc986448242d73",
    'content-type': "application/octet-stream"
    }
	
headers1 = {
    'Ocp-Apim-Subscription-Key': "11824d60fb53420ab9346758b3f181ef",
    'content-type': "application/octet-stream"
    }	

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
   
@app.route('/detect')
def upload_file_object():
   return render_template('upload_object.html')   
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploade_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		data = open(f.filename, 'rb').read()
		response = requests.request("POST", url, headers=headers, data=data)
		output = json.loads(response.text)
		predictions = output['predictions']
		action = predictions[0]['tagName']
		if(action=="Crying"):
			send_mail(action, f.filename)
		return render_template('upload_print.html', state=action)
		#return action
		
@app.route('/uploader_object', methods = ['GET', 'POST'])
def uploade_file_object():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		data = open(f.filename, 'rb').read()
		response = requests.request("POST", url1, headers=headers1, data=data)
		output = json.loads(response.text)
		objects = output['objects']
		x, y, w, h = 0, 0, 0, 0
		for object in objects:
			if object['object'] == "person":
				rectangle = object['rectangle']
				x,y,w,h = rectangle['x'], rectangle['y'], rectangle['w'], rectangle['h']
		print(x,y,w,h)		
		if x<100 and y<450:
			send_mail("in danger location", f.filename)
			return render_template('upload_print.html', state="UnSafe")
		else:		
			return render_template('upload_print.html', state="Safe")		
		
if __name__ == '__main__':
   app.run(debug = True)