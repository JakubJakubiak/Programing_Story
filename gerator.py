import json

# Wczytaj plik JSON do zmiennej
with open('pytanie.json') as f:
  data = json.load(f)

# Zmień wartość pola 'question'
data['question'] = 'Nowe pytanie'

# Zmień opcje odpowiedzi
data['options'] = ['Opcja 1', 'Opcja 2', 'Opcja 3']

# Zmień indeks prawidłowej odpowiedzi
data['answer_index'] = 2

# Zapisz zmienione dane do pliku JSON
with open('pytanie.json', 'w') as f:
  json.dump(data, f)
