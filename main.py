import yaml
from typing import List
from top_calculator import TopCalculator


def load_config(cfg_path: str):
    """
    only yaml is supported as a configuration file
    """
    with open(cfg_path) as file:
        cfg = yaml.load(file, yaml.FullLoader)
    return cfg


def custom_245(datalist: List[int]):
    _min = min(datalist)
    dmin = round(_min / 6 / 100 * 80, 2)

    _max = max(datalist)
    dmax = round(_max / 6 / 100 * 80, 2)

    _avg = round(sum(datalist) / len(datalist), 2)
    davg = round(_avg / 6 / 100 * 80, 2)

    result = f"\n\t\tmin: {_min}({dmin})\n\t\tmax: {_max}({dmax})\n\t\tavg: {_avg}({davg})"
    return result


def custom_s59(datalist: List[int]):
    _max = max(datalist)
    _avg = round(sum(datalist) / len(datalist), 2)
    print(sorted(datalist))

    result = f"\n\tmax: {_max}\n\tavg: {_avg}"
    return result


def custom_deepl(datalist: List[int]):
    _min = min(datalist)
    dmin = round(_min / 8 / 100 * 105, 2)

    _max = max(datalist)
    dmax = round(_max / 8 / 100 * 105, 2)

    _avg = round(sum(datalist) / len(datalist), 2)
    davg = round(_avg / 8 / 100 * 105, 2)

    result = f"\n\t\tmin: {_min}({dmin})\n\t\tmax: {_max}({dmax})\n\t\tavg: {_avg}({davg})"
    return result


cfgs = load_config("./config.yaml")
for cfg in cfgs:
    TopCalculator(cfg, custom_s59).calculate()
