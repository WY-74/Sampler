from typing import List, Dict, Callable, Any


class TopCalculator:
    def __init__(self, cfg: Dict[str, Any], custom_calculator: Callable | None = None) -> None:
        self.data_map = {"pr": 2, "ni": 3, "virt": 4, "res": 5, "shr": 6, "cpu": 8, "mem": 9}
        self.cfg = cfg
        self.file_path = self.cfg["file_path"]
        self.get_custom_value = custom_calculator

    def get_group_by_pid(self):
        def filter(encoding: str = "utf-8"):
            with open(self.file_path, encoding=encoding) as file:
                for line in file:
                    _line = [l.strip() for l in line.split(" ") if l]
                    if _line[0].isdigit() and _line[0] in group:
                        group[_line[0]].append(_line)

        group = {pid.strip(): [] for pid in self.cfg["pid"].split(",")}
        try:
            filter()
        except:
            filter("utf-16-le")
        return group
    
    

    def calculate(self):
        print("#" * 20 + f" {self.file_path} " + "#" * 20)
        # print(f"Start with pid {self.cfg['filter']['pid']}")

        group = self.get_group_by_pid()
        print(group)

        # for ocs in self.cfg["calculate"]:
        #     col, oc = list(ocs.items())[0]
        #     datalist = [float(data[self.data_map[col]]) for data in group if "%" not in data[self.data_map[col]]]
            # # print(datalist)
            # print(f"We have collected {len(datalist)} pieces of data:")
            # # print(f"\t{datalist}\n")
            # print(f"\t{oc} of [{col}]: {getattr(self, f'get_{oc}_value')(datalist)}\n")
