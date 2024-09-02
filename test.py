import yaml

with open("./config.yaml") as f:
    data = yaml.load(f, yaml.FullLoader)

print(data)