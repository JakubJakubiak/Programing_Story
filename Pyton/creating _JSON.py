import os
import random
import json

path = './notes/png'
filenames = []
results = []


for file in os.listdir(path):
    filename, file_extension = os.path.splitext(file)
    filenames.append((filename, file_extension))

for index, (filename, file_extension) in enumerate(filenames):
    options = random.sample([name for i, (name, extension) in enumerate(filenames) if i != index], 3)
  
    answer_index = random.randint(0, 3)
    options.insert(answer_index, filename)
    options = [option.capitalize() for option in options]

    result = {
        "id": index,
        'question': f'lib/logoPng/{filename}{file_extension}',
        'options': options,
        'answer_index': answer_index,
    }

    results.append(result)
    print (result)

with open('result.json', 'w') as f:
    json.dump(results, f)
