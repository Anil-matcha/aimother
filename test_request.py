import requests

url = "https://firstclassification.cognitiveservices.azure.com/customvision/v3.0/Prediction/f7a8c798-b932-4a9d-bfe8-74e4acc3150b/classify/iterations/Iteration1/url"

payload = "{\"Url\": \"https://media.mnn.com/assets/images/2013/09/bigbabysmileonetooth.jpg.653x0_q80_crop-smart.jpg\"}"
headers = {
    'prediction-key': "f725326e539d48adaacc986448242d73",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "6d5064ad-1cf0-97e6-ca48-77a6d45a23dd"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)