# aoc_template.py
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [str(line) for line in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    print(data)

    depth = 0
    horizontal = 0

    for line in data:
        split = line.split(' ')
        print(split[0])
        direction = split[0]
        amount = int(split[1])
        match direction:
            case 'forward':
                horizontal+= amount
            case 'up':
                depth-= amount
            case 'down':
                depth+= amount

    print('Horizontal:'  + str(horizontal))
    print('depth: ' + str(depth))
    print('final product ' + str(horizontal*depth))



def part2(data):
    """Solve part 2"""
    count = 0
    depth = 0
    horizontal = 0
    aim = 0

    for line in data:
        split = line.split(' ')
        print(split[0])
        direction = split[0]
        amount = int(split[1])
        match direction:
            case 'forward':
                horizontal+= amount
                depth += aim*amount
            case 'up':
               aim -= amount
            case 'down':
               aim += amount

    print('Horizontal:'  + str(horizontal))
    print('Depth: ' + str(depth))
    print('Final product ' + str(horizontal*depth))

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        # print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
