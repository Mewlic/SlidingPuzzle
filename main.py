import argparse
from PuzzleSolver import PuzzleSolver


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", "--strategy", type=int, default=2, help="启发函数策略")
    parser.add_argument("-si", "--size", type=int, default='3', help="数字华容道的大小")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    start_state = [5, 3, 6, 1, 8, 4, 7, 2, 0]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    puzzlesolver = PuzzleSolver(args.strategy, args.size)
    path = puzzlesolver.solve_puzzle(start_state, goal_state)

    if path:
        for step, state in enumerate(path):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
