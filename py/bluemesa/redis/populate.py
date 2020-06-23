import os
from bluemesa.util import lineutil
import symboltable
import util

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path_in  = path + '/bluemesa/config/symbols/sdy.txt'
    symbols = lineutil.get_lines_as_set(path_in)
    for symbol in symbols:
        symboltable.write_symbol_to_set("symbol-set-sdy",symbol)
    myset = util.redis_set_to_python_set("symbol-set-sdy")
    print(myset)
