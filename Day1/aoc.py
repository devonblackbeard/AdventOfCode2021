# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]

def part1(data):
  """Solve part 1"""
  count = 0
  for i in range(1, len(data)):
    if int(data[i-1]) < int(data[i]):
      count +=1
  return count

def part2(data):
    """Solve part 2"""

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    # solution2 = part2(data)

    return solution1

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print(solutions)
        # print("\n".join(str(solution) for solution in solutions))
