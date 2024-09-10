# TODO：多设备状态下判断及使用


import os
import subprocess
from typing import List
from utils import vaild_data, get_dmips


class Cell:
    def __init__(self, pids: List[int], filename: str):
        self.pids = pids
        self.filename = filename

    def verify_connection(self):
        response = str(subprocess.check_output("adb devices", shell=True), encoding="utf-8").split("\r\n")[1:]
        devices = []
        for device in response:
            if device.split("\t")[-1] == "device":
                devices.append(device.split("\t")[0])

        if not devices:
            raise Exception("请通过 'abd devices' 检查是否有设备在线!")
        
    def collect(self, filename: str, delay=1, nums=30):
        _pids = ",".join(map(str, self.pids))
        subprocess.call(f"adb shell top -p {_pids} -b -d {delay} -n {nums} > D:/project/top-calculator/temp/{self.filename}.txt", shell=True)

    def get_result(self):
        groups = {str(pid): [] for pid in self.pids}

        with open(os.path.join(os.getcwd(), f"temp\{self.filename}.txt"), encoding="utf-8") as file:
            for line in file:
                _line = [l.strip() for l in line.split(" ") if l]
                if _line[0].isdigit() and _line[0] in groups:
                    groups[_line[0]].append(_line)
            
            for pid in groups:
                print(f"### pid: {pid}, volume: {len(groups[pid])}")
                datalist = []
                for data in groups[pid]:
                    if len(data) != 12:
                        raise Exception(f"数据长度不正确: {data}")
                    datalist.append(float(data[-4]))

                print(datalist)
                self.custom_dmips(datalist)

    def custom_dmips(self, datalist: List[float]):
        _max, _min, datalist = vaild_data(datalist)
        _avg = round(sum(datalist) / len(datalist), 2)

        dmax, dmin, davg = get_dmips([_max, _min, _avg], cpus=6, power=80)  # e245

        result = f"\t\tmin: {_min}({dmin})\n\t\tmax: {_max}({dmax})\n\t\tavg: {_avg}({davg})\n"
        print(result)

        return result