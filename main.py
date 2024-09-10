# import os
# import subprocess
# from typing import List
# from utils import vaild_data, get_dmips



from cell import Cell


cell = Cell(pids=[13065, 1421], filename="test")
# cell.verify_connection()
# cell.collect("test")
cell.get_result()

