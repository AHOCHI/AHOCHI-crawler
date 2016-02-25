import json
json_data = open('TriStateFileIntAlt').read()
data = json.loads(json_data)

print(data)
