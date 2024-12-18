import heapq # Aparrently this is efficient
# def Follow(Coord, Taken = "", Possible = None, Direction = 1, CurrentScore = None):
#     global maze
#     if Possible == None:
#         Coord = (FY, FX)
#         Possible = list()
#     if not (Coord[0] + 1 >= len(maze)) and maze[Coord[0]+1][Coord[1]] == "." and Direction != 3:
#         Possible.append([0, Coord[0]+1, Coord[1]])
#     else: Possible.append(None)
#     if not (Coord[1] + 1 >= len(maze[0])) and maze[Coord[0]][Coord[1]+1] == "." and Direction != 4:
#         Possible.append([1, Coord[0], Coord[1]+1])
#     else: Possible.append(None)
#     if Coord[0] != 0 and maze[Coord[0]-1][Coord[1]] == "." and Direction != 0:
#         Possible.append([2, Coord[0]-1, Coord[1]])
#     else: Possible.append(None)
#     if Coord[1] != 0  and maze[Coord[0]][Coord[1]-1] == "." and Direction != 1:
#         Possible.append([3, Coord[0], Coord[1]-1])
#     else: Possible.append(None)

#     if Possible == (None, None, None, None):
#         return None

#     for i in range(4):
#         LookingDir = (Direction+i)%4
#         if Possible[LookingDir] != None:
#             if i != 0:
#                 Taken += str(LookingDir)
#                 Turns[(Y, X)] = (Taken, Possible, Direction)
#             Follow(Possible[LookingDir])

# def Forward(Coord, Direction = 1, Distance = 0):
#     NY = Coord(0) + DirectionIndex[Direction][0]
#     NX = Coord(1) + DirectionIndex[Direction][1]
#     if 0 <= NY < len(maze) and 0 <= NX < len(maze):
#         if maze[NY][NX] == ".":
#             Distance += 1

    
# def Line(Coord, Direction = 1):
#     breakpoint()
#     global ChoiceLine
#     global ChoiceLocations
#     global maze
#     NY = Coord[0] + DirectionIndex[Direction][0]
#     NX = Coord[1] + DirectionIndex[Direction][1]
#     count = 0
#     while maze[NY][NX] == ".":
#         if maze[NY + DirectionIndex[(Direction+1)%4][0]][NX + DirectionIndex[(Direction+1)%4][1]] == ".":
#             ChoiceLine += str(Direction)
#             ChoiceLocations.append([NY, NX])
#         elif maze[NY + DirectionIndex[(Direction-1)%4][0]][NX + DirectionIndex[(Direction-1)%4][1]] == ".":
#             ChoiceLine += str(Direction)
#             ChoiceLocations.append([NY, NX])
#         maze[NY][NX] = "X"
#         NY += DirectionIndex[Direction][0]
#         NX += DirectionIndex[Direction][1]
#         count += 1

#     if count > 0:
#         if maze[NY + DirectionIndex[(Direction+1)%4][0]][NX + DirectionIndex[(Direction+1)%4][1]] == ".":
#             ChoiceLine += str(Direction)
#             ChoiceLocations.append([NY, NX])
#         elif maze[NY + DirectionIndex[(Direction-1)%4][0]][NX + DirectionIndex[(Direction-1)%4][1]] == ".":
#             ChoiceLine += str(Direction)
#             ChoiceLocations.append([NY, NX])

#     if maze[NY][NX] == "#":
#         NY -= DirectionIndex[Direction][0]
#         NX -= DirectionIndex[Direction][1]

#     if count == 0:
#         ChoiceLocations.pop(-1)
#         ChoiceLine = ChoiceLine[:-1]
#     else:
#         ChoiceLine = ChoiceLine[:-1] + str((int(ChoiceLine[-1])+1)%4)
#     print(ChoiceLine, ChoiceLocations)

#     for i in maze:
#         print(i)
#     Line((ChoiceLocations[-1][0], ChoiceLocations[-1][1]), int(ChoiceLine[-1]))


def NodeFinder(Coord) -> dict[dict]: 
    global graph
    global maze
    # breakpoint()
    temp = {(Coord[0], Coord[1]): {}}
    for i in range(4):
        NY = Coord[0]
        NX = Coord[1]
        steps = 0
        while maze[NY][NX] == "." or maze[NY][NX] == "S":
            NY += DirectionIndex[i][0]
            NX += DirectionIndex[i][1]
            steps += 1
            if i%2 == 0:
                if maze[NY][NX+1] == ".":
                    temp[(Coord[0], Coord[1])][(NY, NX)] = steps + 1000
                if maze[NY][NX-1] == ".":
                    temp[(Coord[0], Coord[1])][(NY, NX)] = steps + 1000
            else:
                if maze[NY+1][NX] == ".":
                    temp[(Coord[0], Coord[1])][(NY, NX)] = steps + 1000
                if maze[NY-1][NX] == ".":
                    temp[(Coord[0], Coord[1])][(NY, NX)] = steps + 1000
            
        if maze[NY][NX] != "S" and maze[NY][NX] != "E":
            NY -= DirectionIndex[i][0]
            NX -= DirectionIndex[i][1]
            steps -= 1
        if maze[NY][NX] != "E":
            temp[(Coord[0], Coord[1])][(NY, NX)] = steps + 1000
        else:
            temp[(Coord[0], Coord[1])][(NY, NX)] = steps
    try:
        temp[(Coord[0], Coord[1])].pop((Coord[0], Coord[1]))
    except:
        pass
    # print(temp)
    # breakpoint()
    return temp
        


    

def DikeStra(FY, FX):
    global graph
    Distances = {(FY, FX): 0}
    Paths = {(FY, FX): [[(FY, FX)]]}
    Visited = set()
    PriorityQ = [(0, (FY, FX))]

    while PriorityQ:
        CDistance, CNode = heapq.heappop(PriorityQ)
        if CNode in Visited:
            continue
        Visited.add(CNode)
        NewNodes = NodeFinder(CNode)
        CacheDict = {}

        for key in set(graph.keys()).union(NewNodes.keys()):
            CacheDict[key] = {**graph.get(key, {}), **NewNodes.get(key, {})}
        graph = dict(CacheDict)

        for NNode, weight in graph.get((CNode)).items():
            distance = CDistance + weight
            if NNode not in Distances or distance < Distances[NNode]:
                Distances[NNode] = distance
                Paths[NNode] = [path + [NNode] for path in Paths[CNode]]
                heapq.heappush(PriorityQ, (distance, NNode))
            elif distance == Distances[NNode]:
                Paths[NNode].extend([path + [NNode] for path in Paths[CNode]])
    return Distances, Paths

def SquareGetter(Nodes):
    global Squares
    for i in range(len(Nodes)-1):
        Node1Y = Nodes[i][0]
        Node1X = Nodes[i][1]
        Node2Y = Nodes[i][0]
        Node2X = Nodes[i][1]

        YDiff = Node2Y - Node1Y
        XDiff = Node2X - Node1X

        if XDiff == 0:
            
        elif YDiff == 0:

        else:
            raise IndexError("There should be some kind of non-difference")




with open("input16.txt" , "r") as f:
    maze = f.readlines()
    DirectionIndex = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(len(maze)):
        maze[i] = list(maze[i].replace("\n", ""))
    # [(Y, X){\Coord of Turn}, DirectionsTaken, Directions possible, CurrentScore]
    Turns = {}
    FX = -1
    FY = -1
    for Y in range(len(maze)):
        for X in range(len(maze[Y])):
            if maze[Y][X] == "S":
                FX = X
                FY = Y

    EX = -1
    EY = -1
    for Y in range(len(maze)):
        for X in range(len(maze[Y])):
            if maze[Y][X] == "E":
                EX = X
                EY = Y

    graph = {}

    # ChoiceLine = ""
    # ChoiceLocations = []
    # Line((FY, FX), 1)
    Please, Routes = DikeStra(FY, FX)
    print(Please[(EY, EX)])
    Routes = Routes.get((EY, EX))
    Squares = []
    for i in Routes:
        print(i)

    # for i in maze:
    #     print(i)