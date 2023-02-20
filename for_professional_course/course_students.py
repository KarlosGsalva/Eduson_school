import csv
import json

with open('students.json', encoding='utf-8') as file, open('data.csv', 'w', encoding='utf-8', newline='') as file_csv:
    writer = csv.writer(file_csv)
    head_list = ['name', 'phone']
    res_list = []
    for i in json.load(file):
        if int(i['age']) > 17 and int(i['progress']) > 74:
            res_list.append([i['name'], i['phone']])
    writer.writerow(head_list)
    writer.writerows(sorted(res_list))
