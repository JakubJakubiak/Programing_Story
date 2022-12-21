import requests
import json
from PIL import Image, ImageEnhance, ImageFilter
import os
import random

path = 'G:/git/pyton/notes/png'

index = 0
randoms = 0

filenames = []
optionss = []
results = []

elements = os.listdir(path)
Foldet_elements = len(elements)


for filename in os.listdir(path):
    # clean_name = os.path.splitext(filename)[0]
    for file in elements:
        filename = os.path.splitext(file)[0]
        filenames.append(filename)

    print(filenames)
   
    randoms=random.randint(0, 3)
    random_elements =  random.sample(filenames, 4) 
    clean_name=random_elements[randoms]

    if(randoms==0): optionss=[clean_name, random_elements[1], random_elements[2], random_elements[3]] 
    if(randoms==1):optionss=[random_elements[0], clean_name, random_elements[2], random_elements[3]]
    if(randoms==2): optionss=[random_elements[0],random_elements[1], clean_name, random_elements[3]]
    if(randoms==3):optionss=[random_elements[0], random_elements[1], random_elements[2], clean_name]

    result = [{
        "id": index,
        'question': 'lib/logoPng/'+clean_name + '.png',
        'options':  optionss,
        'answer_index': randoms,
    }]
            

    results += result
    index = index +1

    with open('result.json', 'w') as f:
        json.dump(results, f)
      
