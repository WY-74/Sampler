import yaml
import time
import subprocess
import concurrent.futures
from typing import Dict, Any


class Sampler:
    def __init__(self):
        self._verify_connection()
        self.configs = self._get_configs()

    def _verify_connection(self):
        response = str(subprocess.check_output("adb devices", shell=True), encoding="utf-8").split("\r\n")[1:]
        devices = []
        for device in response:
            if device.split("\t")[-1] == "device":
                devices.append(device.split("\t")[0])

        if not devices:
            raise Exception("请通过 'abd devices' 检查是否有设备在线!")

        print("设备连接成功!")

    def _get_configs(self):
        with open('config.yaml', 'r') as f:
            configs = yaml.safe_load(f)

        return configs["sampler"]

    def _subprocess_call(self, task: Dict[str, Any]):
        command = f"{task["command"]["command"]} > {self.configs["settings"]["path"]}/{task["name"]}.txt"

        subprocess.call(command, shell=True)
        time.sleep(0.5)
        return True

    def settings(self, cfg: Dict[str, Any]):
        if not cfg["status"]:
            return False

    def run(self):
        tasks = self.configs["tasks"]
        print(f"共发现 {len(tasks)} 个任务!\n")
        print(tasks[0])

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(tasks) + 1) as executor:
            futures = [executor.submit(self._subprocess_call, task) for task in tasks]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(result)


if __name__ == "__main__":
    Sampler().run()
