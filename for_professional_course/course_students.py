import csv
import json

# with open('students.json', encoding='utf-8') as file, open('data.csv', 'w', encoding='utf-8', newline='') as file_csv:
#     writer = csv.writer(file_csv)
#     head_list = ['name', 'phone']
#     res_list = []
#     for i in json.load(file):
#         if int(i['age']) > 17 and int(i['progress']) > 74:
#             res_list.append([i['name'], i['phone']])
#     writer.writerow(head_list)
#     writer.writerows(sorted(res_list))


# Если словарь, переданный методу writer.writerow() , содержит ключ,
# не найденный в именах полей fieldnames, необязательный параметр extrasaction указывает,
# какое действие предпринять.
with open('students.json', encoding='UTF-8') as f:
    data = sorted([d for d in json.load(f) if d['progress'] > 74 and d['age'] > 17], key=lambda x: x['name'])

with open('data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'phone'], extrasaction='ignore')
    writer.writeheader()
    writer.writerows(data)