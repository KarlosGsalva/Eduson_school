import sys
import json

for key, value in json.loads(sys.stdin.read()).items():
    if isinstance(value, list):
        value = ", ".join(map(str, value))
    print(f"{key}: {value}")

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
