import os
import json


class Top:
    def __init__(self, args):
        self.map = {arg: [] for arg in args}
        self.result = []

    def get_file_list(self, dir):
        filelist = []
        for path, _, files in os.walk(dir):
            for file in files:
                if file.endswith(".txt"):
                    filelist.append(f"{path}/{file}")
        return filelist
    
    def parse_txt(self, filepath, encoding):
        with open(filepath, encoding=encoding) as f:
            for line in f:
                for key in self.map:
                    if key in line:
                        data = [data for data in line.strip().replace(f" {key}", "").split(" ") if data]
                        self.map[key].append(float(data[-3]))
                    continue
    
    def calculate(self, info, audit, dmips):
        for key in self.map:
            _avg = round(sum(self.map[key])/len(self.map[key]), 2)
            avg_dmips = round(_avg/audit/100*dmips, 2)
            _max = max(self.map[key])
            max_dmips = round(_max/audit/100*dmips, 2)
            _min = min(self.map[key])
            min_dmips = round(_min/audit/100*dmips, 2)

            info[key]["avg"] = f"{_avg}({avg_dmips})"
            info[key]["max"] = f"{_max}({max_dmips})"
            info[key]["min"] = f"{_min}({min_dmips})"

    def run(self, dir: str, audit: int, dmips: int, **kwargs):
        for file in self.get_file_list(dir):
            info = {key: dict() for key in self.map}
            info["file"] = file

            try:
                self.parse_txt(file, "utf-8")
            except UnicodeDecodeError:
                self.parse_txt(file, "utf-16-le")

            # print(self.map)
            self.calculate(info, audit, dmips)
            self.result.append(info)

        with open(f"{dir}/result.json", "a") as f:
            json.dump(self.result, f, indent=4)
