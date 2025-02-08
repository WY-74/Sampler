import re
import yaml
import subprocess
from time import sleep
from typing import Dict, Any


class Sampler:
    def __init__(self):
        self.tasks = self._init_tasks()

    def _init_tasks(self):
        with open('tasks.yaml', 'r', encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        tasks = cfg.pop("tasks")  # 删除配置文件内tasks字段，其余字段均为全局配置
        for task in tasks:
            task.update(cfg)  # 将全局配置更新到每个task中
            if self._command(task):
                continue

        return tasks

    def _command(self, task: Dict[str, Any]):
        """
        替换command中占位符为对应的值
            task: Dict[str, Any] - 任务字典
        """

        pattern = r'\{(.*?)\}'
        matches = re.findall(pattern, task["command"])

        for key in matches:
            placeholder = '{' + key + '}'
            task["command"] = task["command"].replace(placeholder, task[key])

        return True

    def _subprocess_call(self, task: Dict[str, Any]):
        """
        通过subprocess调用命令
            task: Dict[str, Any] - 任务字典
        """
        for _ in range(task["times"]):
            subprocess.call(task["command"], shell=True)
            sleep(task["delay"])

        print(f"Task <{task['task_name']}> done.")

    def run(self):
        for task in self.tasks:
            self._subprocess_call(task)


if __name__ == "__main__":
    Sampler().run()
