# aoc_template.py
import sys

def checkColumns(row, col, hitCoordList):
    colCount = 0
    for i in range(0,5):
        if([i,col] in hitCoordList):
            colCount += 1
    return colCount

def checkRows(row, col, hitCoordList):
    rowCount = 0
    for i in range(0,5):
        if([row,i] in hitCoordList):
            rowCount += 1
    return rowCount

def checkBingo(row, col, hitCoordList):
    hitColCount = checkColumns(row, col, hitCoordList)
    hitRowCount = checkRows(row, col, hitCoordList)
    if(hitColCount ==5 or hitRowCount ==5):
        return True
    print(hitColCount, hitRowCount)
    return False

def getSumMarkedCoords(hitCoordList, board):
    sum = 0
    for coord in hitCoordList:
        sum += int(board[int(coord[0])][int(coord[1])])
    return sum

def checkBoard(mark, board, hitCoordList):
    # print(board)
    sunk = False
    sum = 0
    lastCalled=-1
    numberCallouts = 0
    for row in board:
        for col in range(0,5):
            sum+= int(row[col])
            numberCallouts +=1
            if(int(row[col]) == mark):
                print('hit')
                lastCalled = int(row[col])
                hitCoordList.append([board.index(row),col])
                sunk = checkBingo(board.index(row), col, hitCoordList)
                if(sunk==True):
                    print("SUNK")
    sumOfMarkedCoords = getSumMarkedCoords(hitCoordList, board)
    # print(sumOfMarkedCoords)
    # print(sunk)
    hitCoordList.clear()
    return (sunk, lastCalled, sum, sumOfMarkedCoords, numberCallouts)

def getFinalScore(lastCalled, sum, sumMarked):
    # print('get final'+ str(lastCalled))
    # print('last called'+ str(lastCalled))
    # print(sum-sumMarked)
    return (sum - sumMarked) * lastCalled


def part1(marks, boards):
  """Solve part 1"""
  hitCoordList = []
  listOfPotentials = []
  finalScore = 0
  for mark in marks:
      for board in boards:
          details= checkBoard(mark, board, hitCoordList)
          if(details[0]== True):
              listOfPotentials.append(details[4])
              print('sunkmate')
              return getFinalScore(details[1], details[2], details[3])
#   return finalScore

def part2(data):
    """Solve part 2"""

def solve(marks, boards):
    """Solve the puzzle for the given input"""

    solution1 = part1(marks, boards)
    return solution1
    # solution2 = part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        file = open(path)

        markedData = file.readline()
        # boardData = file.readlines()[1:]

        marks = ([int(d) for d in markedData.split(',')])
        # boards = [line.strip().split() for line in boardData]
        # boards = [line for line in boardData if line.strip()]
        # lines = list(line for line in (l.strip() for l in boardData))
        fields = [i.strip() for i in file.read().strip().split('\n\n')]
        fields = [i.split('\n') for i in fields]
        fields = [[list(map(int, j.split())) for j in i] for i in fields]

        # print(fields)

        solution = solve(marks,fields)
        print(solution)
        # print("\n".join(str(solution) for solution in solutions))
