def WallCheck(Y, X):
    global GlitchWalls
    for i in range(4):
        if 2 <= Y < len(Race) - 2 and 2 <= X < len(Race[0]) - 2 and Race[Y + DirectionIndex[i][0]][X + DirectionIndex[i][1]] == '#' and Race[Y + (2*DirectionIndex[i][0])][X + (2*DirectionIndex[i][1])] != "#":
            GlitchWalls.append((Y + DirectionIndex[i][0], X + DirectionIndex[i][1]))

with open("input20.txt", "r") as f:
    DirectionIndex = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    Direction = 2
    GlitchWalls = []
    Race = f.readlines()
    Race = list(map(lambda x: x.replace("\n", ""), Race))
    Steps = []
    Xindex = -29
    Yindex = -29
    for i in range(len(Race)):
        if "S" in Race[i]:
            Xindex = Race[i].index("S")
            Yindex = i
            break
    while Race[Yindex][Xindex] != "E":
        WallCheck(Yindex, Xindex)
        Steps.append((Yindex, Xindex))
        while Race[Yindex + DirectionIndex[Direction][0]][Xindex + DirectionIndex[Direction][1]] == '#' or (Yindex + DirectionIndex[Direction][0], Xindex + DirectionIndex[Direction][1]) in Steps:
            Direction = (Direction+1)%4
        Yindex += DirectionIndex[Direction][0]
        Xindex += DirectionIndex[Direction][1]
        # print(len(Steps), Yindex, Xindex)
    print(Steps)










