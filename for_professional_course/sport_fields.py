import csv
import json

with open('playgrounds.csv', 'r', encoding='utf-8') as file:
    file = csv.DictReader(file, delimiter=';')
    d = {}
    for i in file:
        d.setdefault(i['AdmArea'], dict()).setdefault(i['District'], []).append(i['Address'])

with open('addresses.json', 'w', encoding='utf-8') as file_w:
    json.dump(d, file_w, ensure_ascii=False)
