import os
import sys
import glob

list_of_files = glob.glob('solutions/**/')

latest_sol_module = max(list_of_files, key=os.path.getmtime)

sys.path = [os.path.dirname(latest_sol_module)] + ["."] + sys.path


def test_sol():
    print(sys.path)
    import sol
