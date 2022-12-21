import requests
import json
from PIL import Image, ImageEnhance, ImageFilter
import os
import random

path = 'G:/git/pyton/notes/png'

index = 0
randoms = 0

filenames = []
results = []

elements = os.listdir(path)
Foldet_elements = len(elements)


for filename in os.listdir(path):
    for file in elements:
        filename = os.path.splitext(file)[0]
        filenames.append(filename)

    print(filenames)
   
    randoms=random.randint(0, 3)
    random_elements =  random.sample(filenames, 4) 
    clean_name = random_elements[randoms]

    result = [{
        "id": index,
        'question': 'lib/logoPng/'+clean_name + '.png',
        'options':  random_elements,
        'answer_index': randoms,
    }]
            

    results += result
    index = index +1

    with open('result.json', 'w') as f:
        json.dump(results, f)
      
