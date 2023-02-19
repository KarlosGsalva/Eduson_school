import json

"""method 1"""
# with open('for_professional_course/people.json', 'r', encoding='utf-8') as file:
#     data1 = json.load(file)
#     keys_data = (max(data1, key=len)).keys()
#     new_data = []
#
#     for i in data1:
#         d = {}
#         for k in keys_data:
#             d[k] = i.get(k, None)
#         new_data.append(d)
#
# with open('updated_people.json', 'w', encoding='utf-8') as w_file:
#     json.dump(new_data, w_file)

"""method 2"""
# with open('people.json', encoding='utf8') as file, open('updated_people.json', 'w') as w_file:
#     people = json.load(file)
#     d = {k: None for i in people for k in i.keys()}
#     json.dump([d | i for i in people], w_file)

"""method 3"""
with open('people.json', 'r', encoding='utf-8') as r, open('updated_people.json', 'w', encoding='utf-8') as w:
    data = json.load(r)
    all_keys = set(key for i in data for key in i.keys())
    json.dump([i | dict.fromkeys(all_keys - i.keys(), None) for i in data], w)
