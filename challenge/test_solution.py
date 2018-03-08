import sys
import reproducible_seed

with open("solution_test.txt") as f:
    solution_module = f.read().strip()

sys.path = [solution_module] + ["."] + sys.path


def test_sol():
    print(sys.path)
    import sol
