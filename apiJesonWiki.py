import requests
import json

api_url = 'https://pl.wikipedia.org/w/api.php'

params = {
    'action': 'query',
    'format': 'json',
    'prop': 'pageimages',
    'piprop': 'original',
    'titles': 'Apple'
}

response = requests.get(api_url, params=params)
data = response.json()

pageid = list(data['query']['pages'].keys())[0]
image_url = data['query']['pages'][pageid]
# ['original']['source']

print(image_url)
print(data)

result = {
    "id": 15,
    'question': image_url,
    'options':  ['Nike', 'Adidas', 'Puma', 'Reebok'],
    'answer_index': 1,
    
}

print(result)

with open('result.json', 'w') as f:
    json.dump(result, f)