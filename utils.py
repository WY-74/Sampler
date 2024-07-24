from typing import List


def vaild_data(datalist: List[float], accept_zero: bool = True):
    # 返回最大值，最小值，除去最大值最小值之后的数据列
    if not accept_zero:
        datalist = [x for x in datalist if x != 0]

    _max = max(datalist)
    _min = min(datalist)

    datalist = [x for x in datalist if x != _max and x != _min]
    return _max, _min, datalist


def get_dmips(datalist: List[float], cpus: int, power: int):
    return [round(data / cpus / 100 * power, 2) for data in datalist]
