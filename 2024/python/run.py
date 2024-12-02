import argparse
import importlib

from utils import AOCSolution

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("day", type=int, help="Day to run")
    parser.add_argument("part", type=int, help="Part to run", choices=[1, 2])

    args = parser.parse_args()

    print(f"Solution for day {args.day}, part {args.part}")

    solution_cls: AOCSolution = getattr(
        importlib.import_module(f"solutions.day_{args.day:02d}"), "Solution"
    )
    input_file = f"../inputs/day_{args.day:02d}.txt"

    solution = solution_cls(input_file)
    result = solution.solve(args.part)

    print(f"Result: {result}")
