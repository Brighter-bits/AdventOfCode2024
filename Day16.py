def Follow(Coord, Taken = "", Possible = None, Direction = 1, CurrentScore = None):
    global maze
    if Possible == None:
        Coord = (FY, FX)
        Possible = list()
    if not (Coord[0] + 1 >= len(maze)) and maze[Coord[0]+1][Coord[1]] == "." and Direction != 3:
        Possible.append([0, Coord[0]+1, Coord[1]])
    else: Possible.append(None)
    if not (Coord[1] + 1 >= len(maze[0])) and maze[Coord[0]][Coord[1]+1] == "." and Direction != 4:
        Possible.append([1, Coord[0], Coord[1]+1])
    else: Possible.append(None)
    if Coord[0] != 0 and maze[Coord[0]-1][Coord[1]] == "." and Direction != 0:
        Possible.append([2, Coord[0]-1, Coord[1]])
    else: Possible.append(None)
    if Coord[1] != 0  and maze[Coord[0]][Coord[1]-1] == "." and Direction != 1:
        Possible.append([3, Coord[0], Coord[1]-1])
    else: Possible.append(None)

    if Possible == (None, None, None, None):
        return None

    for i in range(4):
        LookingDir = (Direction+i)%4
        if Possible[LookingDir] != None:
            if i != 0:
                Taken += str(LookingDir)
                Turns[(Y, X)] = (Taken, Possible, Direction)
            Follow(Possible[LookingDir])

def Forward(Coord, Direction = 1, Distance = 0):
    NY = Coord(0) + DirectionIndex[Direction][0]
    NX = Coord(1) + DirectionIndex[Direction][1]
    if 0 <= NY < len(maze) and 0 <= NX < len(maze):
        if maze[NY][NX] == ".":
            Distance += 1

    

    




with open("input16.txt" , "r") as f:
    maze = f.readlines()
    DirectionIndex = [(1, 0), (1, 0), (-1, 0), (0, -1)]
    for i in range(len(maze)):
        maze[i] = list(maze[i].replace("\n", ""))
    # [(Y, X){\Coord of Turn}, DirectionsTaken, Directions possible, CurrentScore]
    Turns = {}
    FX = -1
    FY = -1
    for Y in range(maze):
        for X in range(maze[Y]):
            if maze[Y][X] == "S":
                FX = X
                FY = Y

    EX = -1
    EY = -1
    for Y in range(maze):
        for X in range(maze[Y]):
            if maze[Y][X] == "E":
                EX = X
                EY = Y

    print(maze)