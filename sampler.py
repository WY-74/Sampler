import yaml
import time
import subprocess
import concurrent.futures


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

        print("connection successful!")

    def _get_configs(self):
        with open('config.yaml', 'r') as f:
            configs = yaml.safe_load(f)

        return configs["sampler"]

    def _subprocess_call(self, command, times: int = 60, delay: int = 1):
        path = command.split(">>")[1].strip()
        if self.configs["cut"]:
            delimiter = f'{"-" * 50}'
        else:
            delimiter = ""

        for _ in range(times):
            subprocess.call(command, shell=True)
            subprocess.call(f"echo {delimiter} >> {path}", shell=True)
            time.sleep(delay)
        return True

    def _get_commands(self):
        path = self.configs["path"]
        name = self.configs["name"]
        tags = self.configs["tags"]
        commands = self.configs["commands"]

        if len(tags) != len(commands):
            raise Exception("tags 和 commands 的长度不一致!")

        return [f"{command} >> {path}/{name}_{tags[index]}.txt" for index, command in enumerate(commands)]

    def run(self):
        commands = self._get_commands()
        times = self.configs["times"]
        delay = self.configs["delay"]

        max_workers = len(commands) + 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(self._subprocess_call, command, times, delay) for command in commands]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(result)


if __name__ == "__main__":
    Sampler().run()
