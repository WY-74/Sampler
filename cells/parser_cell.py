class Parser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.groups = self._init_groups()

    def _get_effective_data(self):
        effective_data = []

        with open(self.file_path, encoding="utf-8") as f:
            for line in f:
                _line = [l.strip() for l in line.split(" ") if l]
                if _line[0].isdigit():
                    # 通常情况下每一条应分割出12条数据，如果不是则说明该条数据的args中有空格存在
                    if len(_line) != 12:
                        _line[-2] = _line[-2] + " " + _line[-1]
                        _line.pop()
                    effective_data.append(_line)

        return effective_data

    def _init_groups(self):
        effective_data = self._get_effective_data()
        groups = {}

        for data in effective_data:
            if data[0] not in groups:
                groups[data[0]] = {"arg": data[-1], "data": []}
            groups[data[0]]["data"].append(data[1:-1])

        return groups

    def calculator(self, func):
        return func().run(self.groups)
