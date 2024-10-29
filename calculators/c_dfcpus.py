"""
东风性能统计
展示完整数据列表，cpu最大值和平均值
在均值计算过程中，排除最大值和最小值；所有数据均精确到两位小数
"""

from typing import List


class DFcpus:
    def _get_effective_cpus(self, cpus: List[float], accept_zero: bool = True):
        if not accept_zero:
            cpus = [x for x in cpus if x != 0]

        _max = max(cpus)
        _min = min(cpus)

        cpus = [x for x in cpus if x != _max and x != _min]
        cpus.sort()
        return _max, cpus

    def run(self, groups):
        results = ""

        for k in groups.keys():
            results += f"##### {k} [{groups[k]['arg']}][{len(groups[k]['data'])}] #####\n"

            cpus = [float(i[7]) for i in groups[k]["data"]]
            _max, cpus = self._get_effective_cpus(cpus)
            _avg = round(sum(cpus) / len(cpus), 2)

            results += f"{cpus}\n\t\tmax: {_max}\n\t\tavg: {_avg}\n\n"

        print(results)
