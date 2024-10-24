import os
import subprocess

from calculator import Calculator


class Cell:
    def __init__(self, pids: str, delay: int, nums: int, filename: str, cpus: int, power: int):
        self.pids = pids
        self.delay = delay
        self.nums = nums
        self.filename = filename
        self.cpus = cpus
        self.power = power
        self.calculator = Calculator()

    def verify_connection(self):
        response = str(subprocess.check_output("adb devices", shell=True), encoding="utf-8").split("\r\n")[1:]
        devices = []
        for device in response:
            if device.split("\t")[-1] == "device":
                devices.append(device.split("\t")[0])

        if not devices:
            raise Exception("请通过 'abd devices' 检查是否有设备在线!")

        print("connection successful")

    def collect(self):
        command = f"adb shell top -p {self.pids} -b -d {self.delay} -n {self.nums} > D:/project/top-calculator/temp/{self.filename}.txt"
        print(command)
        subprocess.call(command, shell=True)

    def get_result(self, resort: bool = False):
        groups = {pid: [] for pid in self.pids.split(",")}

        with open(os.path.join(os.getcwd(), f"temp\\{self.filename}.txt"), encoding="utf-8") as file:
            for line in file:
                _line = [l.strip() for l in line.split(" ") if l]
                if _line[0].isdigit() and _line[0] in groups:
                    groups[_line[0]].append(_line)

            for pid in groups:
                print(f"##### pid: {pid}, volume: {len(groups[pid])} #####")
                datalist = []
                for data in groups[pid]:
                    datalist.append(float(data[8]))

                self.calculator.custom_dmips(datalist, self.cpus, self.power, resort)
