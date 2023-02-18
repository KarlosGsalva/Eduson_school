import json


"""method #1"""
with open('data.json', 'r', encoding='utf-8') as o_file:
    r_file = json.load(o_file)
    new_list = []
    for i in r_file:
        if isinstance(i, str):
            new_list.append(i + '!')
        elif type(i) == int:
            new_list.append(i + 1)
        elif i in (True, False):
            if i is True:
                new_list.append(False)
            elif i is False:
                new_list.append(True)
        elif isinstance(i, list):
            new_list.append(i * 2)
        elif isinstance(i, dict):
            i.update({'newkey': None})
            new_list.append(i)
        elif i is None:
            continue
with open('updated_data.json', 'w') as c_file:
    json.dump(new_list, c_file)


"""method #2"""
with open('data.json', encoding='utf-8') as file:
    data_json = json.load(file)

updated_data = []
for value in data_json:
    match value:
        case str(): value += '!'
        case bool(): value = not value
        case int(): value += 1
        case list(): value *= 2
        case dict(): value["newkey"] = None
        case None: continue
    updated_data.append(value)

with open('updated_data.json', 'w', encoding='utf-8') as file:
    json.dump(updated_data, file)


"""method #3"""
with open('data.json') as file_in, open('updated_data.json', 'w') as file_out:

    lst = []
    data = json.load(file_in)
    for value in data:
        if type(value) == str:
            lst.append(value + '!')
        elif type(value) in [int, float]:
            lst.append(value + 1)
        elif type(value) == bool:
            lst.append(not value)
        elif type(value) == list:
            lst.append(value * 2)
        elif type(value) == dict:
            lst.append(value | {"newkey": None})
        elif value is None:
            pass

    json.dump(lst, file_out)