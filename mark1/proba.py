import requests, json


data = {'source': 'ленточный конвейер'}
s = requests.get(r'https://fasttranslator.herokuapp.com/api/v1/detect', params=data)

data = s.json()

print(data['Lang'])