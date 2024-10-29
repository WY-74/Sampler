import time
import subprocess
import concurrent.futures


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

        return ",".join(_pids), ",".join(_detial_ids)

    def _subprocess_call(self, command):
        subprocess.call(command, shell=True)
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
            commands.append(
                f"adb shell top -p {self.detial_ids} -b -H {self.others} > temp/{self.file_name}_thread.txt"
            )

            max_workers = len(self.detial_ids) + 1
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [executor.submit(self._subprocess_call, command) for command in commands]
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    print(result)
            return
        else:
            result = self._subprocess_call(command)
            print(result)
