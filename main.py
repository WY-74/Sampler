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

    result = f"\n\t\tmin: {_min}({dmin})\n\t\tmax: {_max}({dmax})\n\t\tavg{_avg}({davg})"
    return result


cfgs = load_config("D:/work/auto-performance/config.yaml")
for cfg in cfgs:
    TopCalculator(cfg, custom_245).calculate()
