from utils import get_config
from top import Top
from meminfo import Meminfo


confs = get_config()
options = confs["options"]
RUN = {"top": Top, "meminfo": Meminfo}

def main(option, conf):
    print(conf)
    return RUN[option](conf["args"])

if __name__ == "__main__":
    for option in options:
        for conf in confs[option]:
            print(id(main(option, conf)))
            # main(option, conf)
