import json
import sys

data = json.loads(sys.stdin.read())
for k, v in data.items():
    if isinstance(v, list):
        print(f'{k}: {", ".join(map(str, v))}')
    else:
        print(f'{k}: {v}')

"""
Test data
{
"src": "Images/Sun.png",
"name": "sun1",
"hOffset": 250,
"AAA": ["ABC", 123, 123, "XYZ"],
"vOffset": 250,
"alignment": "center",
"key": [1, 2, 3, 4, 5],
"another_key": ["a", "b", "c"]
}
"""
