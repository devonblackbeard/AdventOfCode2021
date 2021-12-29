# aoc_template.py

import decimal
import pathlib
import sys
import copy
import math
import statistics

def parse(puzzle_input):
    """Parse input"""
    return [str(line) for line in puzzle_input.split()]

def getMode(column):
    return statistics.mode(column)

def getModeOxygen(column):
    numZero = column.count(0)
    numOne = column.count(1)
    if(numZero>numOne):
        return 0
    elif (numOne> numZero):
        return 1
    else:
        return 1

def getLeastCommon(column):
    numZero = column.count(0)
    numOne = column.count(1)
    if(numZero>numOne):
        return 1
    elif (numOne> numZero):
        return 0
    else:
        return 0

def getDecimalForm(binaryForm):
    stringInts = [str(int) for int in binaryForm]
    gammaString = ''.join(stringInts)
    return int(gammaString,2)

def getEpsilonFromGamma(gammaArray):
    epsilonArray = copy.deepcopy(gammaArray)
    for i in range(0, len(gammaArray)):
        epsilonArray[i] = 1- gammaArray[i]
    return epsilonArray

def getGammaRate(data):
    gammaRate = []
    gammaArray = []

    for i in range(0,len(data[0])):
        for gammaValue in data:
            gammaArray.append(int(gammaValue[i]))

        if(len(gammaArray) == len(data)):
            gammaRate.append(getMode(gammaArray))
            gammaArray.clear()

    return gammaRate

def part1(data):
    """Solve part 1"""
    gammaRate = getGammaRate(data)
    epsilonRate= getEpsilonFromGamma(gammaRate)

    return getDecimalForm(gammaRate) * getDecimalForm(epsilonRate)

def getDataStartsWithOne(data,index):
    startWithOneArray = []
    for col in data:
        if (col[index] == str(1)):
            startWithOneArray.append(col)
    return startWithOneArray

def getDataStartsWithZero(data, index):
    startWithZeroArray = []
    for col in data:
        if (col[index] == str(0)):
            startWithZeroArray.append(col)
    return startWithZeroArray

def getOxygenRating(data):
    col = []
    numIterations = len(data[0])
    newData = copy.deepcopy(data)

    for i in range(0,numIterations):
        for row in newData:
            col.append(int(row[i]))

        if(len(col) == len(newData) and len(newData) >1):
            mostCommon = getModeOxygen(col)

            if(mostCommon ==1):
                newData = getDataStartsWithOne(newData, i)
            else:
                newData = getDataStartsWithZero(newData, i)
            col.clear()
    return getDecimalForm(newData)

def getCarbonRating(data):
    col = []
    numIterations = len(data[0])
    newData = copy.deepcopy(data)

    for i in range(0,numIterations):
        for row in newData:
            col.append(int(row[i]))

        if(len(col) == len(newData) and len(newData) >1):
            leastCommon = getLeastCommon(col)

            if(leastCommon ==1):
                newData = getDataStartsWithOne(newData, i)
            else:
                newData = getDataStartsWithZero(newData, i)
            col.clear()

    return getDecimalForm(newData)

def part2(data):
    """Solve part 2"""
    oxygenRating = getOxygenRating(data)
    carbonRating = getCarbonRating(data)

    return oxygenRating * carbonRating

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
