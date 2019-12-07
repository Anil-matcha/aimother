from flask import Flask, render_template, request
from werkzeug import secure_filename
import requests
import json
url = "https://firstclassification.cognitiveservices.azure.com/customvision/v3.0/Prediction/f7a8c798-b932-4a9d-bfe8-74e4acc3150b/classify/iterations/Iteration1/image"

headers = {
    'prediction-key': "f725326e539d48adaacc986448242d73",
    'content-type': "application/octet-stream"
    }

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
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
		return action
		
if __name__ == '__main__':
   app.run(debug = True)