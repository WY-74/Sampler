import yaml
from typing import List
from top_calculator import TopCalculator
from utils import vaild_data, get_dmips


def load_config(cfg_path: str):
    """
    only yaml is supported as a configuration file
    """
    with open(cfg_path) as file:
        cfg = yaml.load(file, yaml.FullLoader)
    return cfg


def custom_dmips(datalist: List[float]):
    _max, _min, datalist = vaild_data(datalist)
    _avg = round(sum(datalist) / len(datalist), 2)

    dmax, dmin, davg = get_dmips([_max, _min, _avg], cpus=6, power=80)  # e245

    result = f"\n\t\tmin: {_min}({dmin})\n\t\tmax: {_max}({dmax})\n\t\tavg: {_avg}({davg})"

    return result


def custom_dongfeng(datalist: List[int]):
    _max, _, datalist = vaild_data(datalist)
    _avg = round(sum(datalist) / len(datalist), 2)
    print(sorted(datalist))

    result = f"\n\tmax: {_max}\n\tavg: {_avg}"
    return result


if __name__ == "__main__":
    cfgs = load_config("./config.yaml")
    for cfg in cfgs:
        TopCalculator(cfg, custom_dmips).calculate()
