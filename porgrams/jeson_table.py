import os
import random
import json

# path = './notes/png'

# index = 0
# randoms = 0

# filenames = []
# results = []


# for file in os.listdir(path):
#     filename = os.path.splitext(file)[0]
#     filenames.append(filename)

# for filename in os.listdir(path):
#     randoms = random.randint(0, 3)
#     random_elements = random.sample(filenames, 4)
#     random_elements[randoms] = filenames[index]

#     result = [{
#         "id": index,
#         'question': f'lib/logoPng/{filenames[index]}.png',  
#         'options':  random_elements,
#         'answer_index': randoms,
#     }]

#     results += result
#     index = index + 1
#     print(result)

#     with open('result.json', 'w') as f:
#         json.dump(results, f)




# ///AI Kod 


path = './notes/png'
filenames = []
results = []

# Pobierz nazwy plików z katalogu
for file in os.listdir(path):
    filename, file_extension = os.path.splitext(file)
    filenames.append((filename, file_extension))

# Dla każdej nazwy pliku utwórz obiekt z pytaniem i opcjami odpowiedzi
for index, (filename, file_extension) in enumerate(filenames):
    # Losuj 4 opcje odpowiedzi z listy nazw plików (z wyjątkiem bieżącego)
    options = random.sample([name for i, (name, extension) in enumerate(filenames) if i != index], 3)
    # Losuj indeks poprawnej odpowiedzi
    answer_index = random.randint(0, 3)
    # Wstaw poprawną odpowiedź do listy opcji
    options.insert(answer_index, filename)

    result = {
        "id": index,
        'question': f'lib/logoPng/{filename}{file_extension}',
        'options': options,
        'answer_index': answer_index,
    }

    results.append(result)
    print (result)

# Zapisz wyniki do pliku json
with open('result.json', 'w') as f:
    json.dump(results, f)
