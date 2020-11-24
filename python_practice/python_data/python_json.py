import json

dict_h = {
    "a" : [1, 2, 3],
    "name" : ["spider man", "star"]
}

with open("data.json", "w") as f:
    json.dump(dict_h, f)

print(json.dumps(dict_h))
print(type(json.dumps(dict_h)))

json_load = json.load(open("data.json"))
print(json_load)