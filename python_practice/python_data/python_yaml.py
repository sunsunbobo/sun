import yaml

print(yaml.safe_load(open("data.yaml")))

print(yaml.safe_load(open("data2.yaml")))

a = [[{'a': 1}, 'admin2'], 'admin3']

with open("datayml.yaml", "w") as f:
    yaml.dump(a, f)