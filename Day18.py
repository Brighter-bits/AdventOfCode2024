from collections import deque # This might be useful I don't know
from copy import deepcopy
def FloodFill(Queue):
    global Squares
    global NextSquares
    global TempGrid
    for i in range(len(Queue)):
        TempGrid[Queue[i][1]][Queue[i][0]] = "X"
        for j in range(4):
            NX = Queue[i][0] + Directions[j][1]
            NY = Queue[i][1] + Directions[j][0]
            if 0 <= NY < len(TempGrid) and 0 <= NX < len(TempGrid[0]) and TempGrid[NY][NX] != "X" and TempGrid[NY][NX] != "#":
                NextSquares.append((NX, NY))
                TempGrid[NY][NX] = "X"
        

def P1():
    global Squares
    global NextSquares
    global Grid
    global count
    global TempGrid
    for i in range(1024):
        TempGrid[Bytes[i][1]][Bytes[i][0]] = "#"
    while TempGrid[70][70] != "X":
        FloodFill(Squares)
        Squares = deque(NextSquares)
        NextSquares = deque()
        count += 1
        print(Squares)
    print(count)

def P2():
    global Squares
    global NextSquares
    global Grid
    global count
    global TempGrid
    count = 2200
    while True:
        TempGrid = deepcopy(Grid)
        # if count == 2:
        #     breakpoint()
        for i in range(count):
            TempGrid[Bytes[i][1]][Bytes[i][0]] = "#"
        Possible = False
        Squares = deque()
        Squares.append((0, 0))
        while len(Squares) != 0:
            FloodFill(Squares)
            Squares = deque(NextSquares)
            NextSquares = deque()
            # print(Squares)
        if TempGrid[70][70] == "X":
            Possible = True
        if not Possible:
            breakpoint()
            break
        count += 1
        print(count)
    print(count, Bytes[count])


with open("input18.txt", "r") as f:
    Directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    input = f.readlines()
    Bytes = list(map(lambda x: x.split(","), input))
    for i in range(len(Bytes)):
        Bytes[i] = list(map(int, Bytes[i]))
    print(Bytes)

    Grid = [["." for a in range(71)] for b in range(71)]

    Squares = deque()
    Squares.append((0, 0))
    NextSquares = deque()
    count = 0
    TempGrid = deepcopy(Grid)
    # P1()
    P2()
    


    
