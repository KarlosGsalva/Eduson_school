import json


with open('countries.json', encoding='utf-8') as file_o:
    d = {}
    for i in json.load(file_o):
        country, religion = i.values()
        d.setdefault(religion, []).append(country)

with open('religion.json', 'w', encoding='utf-8') as file_w:
    json.dump(d, file_w)
