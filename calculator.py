from typing import List

#    PID USER         PR  NI VIRT  RES  SHR S[%CPU] %MEM     TIME+ ARGS
#    868 root         20   0 160M  16M  11M S 25.9   0.1   4:28.32 android.hardware.audio.service


class E245Dmips:
    def _get_effective_cpus(self, cpus: List[float], accept_zero: bool = True):
        if not accept_zero:
            cpus = [x for x in cpus if x != 0]

        _max = max(cpus)
        _min = min(cpus)

        cpus = [x for x in cpus if x != _max and x != _min]
        return _max, _min, cpus

    def _get_dmips(self, cpus: List[float]):
        return [round(cpu / 8 / 100 * 60, 2) for cpu in cpus]

    def run(self, groups):
        """
        用于吉利E245算力统计
        N dmips = cpus% / 6 / 100 * 80
        在均值计算过程中，排除最大值和最小值；所有数据均精确到两位小数
        """
        results = ""

        for k in groups.keys():
            results += f"##### {k} [{groups[k]["arg"]}][{len(groups[k]["data"])}] #####\n"

            cpus = [float(i[7]) for i in groups[k]["data"]]
            _max, _min, cpus = self._get_effective_cpus(cpus)
            _avg = round(sum(cpus) / len(cpus), 2)

            dmax, dmin, davg = self._get_dmips([_max, _min, _avg])
            results += f"\t\tmin: {_min}({dmin})\n\t\tmax: {_max}({dmax})\n\t\tavg: {_avg}({davg})\n\n"

        print(results)
