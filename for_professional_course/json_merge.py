import json

with open('data1.json', 'r', encoding='utf-8') as data1, open('data2.json', 'r', encoding='utf-8') as data2:
    data1p = json.load(data1)
    data2p = json.load(data2)

with open('data_merge.json', 'w', encoding='utf-8') as w_file:
    json.dump(data1p | data2p, w_file)

