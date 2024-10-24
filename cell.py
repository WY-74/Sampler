import os
import time
import subprocess
import concurrent.futures

from calculator import Calculator


class Sampler:
    def __init__(self, pids: str, file_name: str, others: str):
        self.pids, self.detial_ids = self._parse_pids(pids)
        self.file_name = file_name
        self.others = others

    def _parse_pids(self, pids: str):
        _pids = []
        _detial_ids = []

        for pid in pids.split(","):
            if "+" in pid.strip():
                pid = pid.replace("+", "").strip()
                _pids.append(pid)
                _detial_ids.append(pid)
            else:
                _pids.append(pid.strip())

        return ",".join(_pids), "".join(_detial_ids)

    def _subprocess_call(self, command):
        subprocess.call(command, shell=True)
        print(time.time_ns())
        return f"successfully executed[{time.time_ns()}]: {command}"

    def verify_connection(self):
        response = str(subprocess.check_output("adb devices", shell=True), encoding="utf-8").split("\r\n")[1:]
        devices = []
        for device in response:
            if device.split("\t")[-1] == "device":
                devices.append(device.split("\t")[0])

        if not devices:
            raise Exception("请通过 'abd devices' 检查是否有设备在线!")

        print("connection successful!")

    def collect(self):
        command = f"adb shell top -p {self.pids} -b {self.others} > temp/{self.file_name}.txt"
        if self.detial_ids:
            commands = [command]
            commands.append(f"adb shell top -p {self.pids} -b -H {self.others} > temp/{self.file_name}_thread.txt")

            max_workers = len(self.detial_ids) + 1
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [executor.submit(self.subprocess_call, command) for command in commands]
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    print(result)
            return
        else:
            result = self.subprocess_call(command)
            print(result)


class Parser:
    def __init__(self, pids: str, file_path: str):
        self.groups = self._parse_pids(pids)
        self.file_path = file_path

    def _parse_pids(self, pids: str):
        return {pid.strip(): [] for pid in pids.split(",")}

    def fill_groups(self):
        with open(self.file_path, encoding="utf-8") as file:
            for line in file:
                print(line)
                # _line = [l.strip() for l in line.split(" ") if l]
                # if _line[0].isdigit() and _line[0] in self.groups:
                #     self.groups[_line[0]].append(_line)

    def calculator(self):
        pass


class Cell:
    def __init__(self, pids: str, file_name: str, others: str):
        self.pids, self.detial_ids = self._parse_pids(pids)
        self.file_name = file_name
        self.others = others
        self.calculator = Calculator()

    def get_result(self, resort: bool = False):
        # groups = {pid: [] for pid in self.pids.split(",")}

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

                self.calculator.custom_dmips(datalist, 8, 60, resort)
