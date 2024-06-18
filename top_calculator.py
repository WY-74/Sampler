from typing import List, Dict, Callable, Any


class TopCalculator:
    def __init__(self, cfg: Dict[str, Any], custom_calculator: Callable | None = None) -> None:
        self.data_map = {"pr": 2, "ni": 3, "virt": 4, "res": 5, "shr": 6, "cpu": 8, "mem": 9}
        self.cfg = cfg
        self.file_path = self.cfg["file_path"]
        self.get_custom_value = custom_calculator

    def get_group_by_filter(self):
        filter, value = list(self.cfg["filter"].items())[0]
        group = []
        try:
            with open(self.file_path, encoding="utf-8") as file:
                lines = getattr(self, f"filter_by_{filter}")(file, str(value))
        except Exception:
            with open(self.file_path, encoding="utf-16-le") as file:
                lines = getattr(self, f"filter_by_{filter}")(file, str(value))

        for line in lines:
            line = [l for l in line.split(" ") if l]
            group.append(line)

        return group

    def filter_by_pid(self, file, pid: str):
        lines = []
        for line in file:
            line = line.strip()
            if pid in line and line[0].isdigit():
                lines.append(line)
        return lines

    def filter_by_user(self, file, user: str):
        lines = []
        for line in file:
            line = line.strip()
            if line and line.split(" ")[1] == user:
                lines.append(line)

        return lines

    def get_max_value(self, datalist: List[int]):
        return round(max(datalist), 2)

    def get_min_value(self, datalist: List[int]):
        return round(min(datalist), 2)

    def get_avg_value(self, datalist: List[int]):
        return round(sum(datalist) / len(datalist), 2)

    def calculate(self):
        print("#" * 20 + f" {self.file_path} " + "#" * 20)
        print(f"Start with pid {self.cfg['filter']['pid']}")

        group = self.get_group_by_filter()

        for ocs in self.cfg["calculate"]:
            col, oc = list(ocs.items())[0]
            datalist = [float(data[self.data_map[col]]) for data in group if "%" not in data[self.data_map[col]]]
            # print(datalist)
            print(f"We have collected {len(datalist)} pieces of data:")
            # print(f"\t{datalist}\n")
            print(f"\t{oc} of [{col}]: {getattr(self, f'get_{oc}_value')(datalist)}\n")
