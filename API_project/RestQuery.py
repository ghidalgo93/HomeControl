import requests
import json

url = 'http://127.0.0.1:5000/' #local IP, I'm pretty sure
payload = {
        'plants' : {
            'water' : True,
            'moisture' : False
            },
        'lights' : {
            'on' : True
            }
        }
response = requests.post(url,json=payload).json()
print response
