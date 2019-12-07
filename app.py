from flask import Flask
app = Flask(__name__)

@app.route('/')
def upload_file():
   return "Success"
		
if __name__ == '__main__':
   app.run(debug = True)