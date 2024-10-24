from typing import List


class Calculator:
    def _vaild_data(self, datalist: List[float], accept_zero: bool = True):
        # 返回最大值，最小值，除去最大值最小值之后的数据列
        if not accept_zero:
            datalist = [x for x in datalist if x != 0]

        _max = max(datalist)
        _min = min(datalist)

        datalist = [x for x in datalist if x != _max and x != _min]
        return _max, _min, datalist

    def _get_dmips(self, datalist: List[float], cpus: int, power: int):
        return [round(data / cpus / 100 * power, 2) for data in datalist]

    def custom_dmips(self, datalist: List[float], cpus: int, power: int, resort: bool = False):
        _max, _min, datalist = self._vaild_data(datalist)
        _avg = round(sum(datalist) / len(datalist), 2)

        dmax, dmin, davg = self._get_dmips([_max, _min, _avg], cpus, power)

        result = f"\t\tmin: {_min}({dmin})\n\t\tmax: {_max}({dmax})\n\t\tavg: {_avg}({davg})\n"
        if resort:
            datalist.sort()
        print(datalist)
        print(result)
