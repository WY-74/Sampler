import yaml


def get_config(filepath: str = "./config.yaml"):
    with open(filepath, "r") as f:
        confs = yaml.load(f, yaml.FullLoader)
    return confs