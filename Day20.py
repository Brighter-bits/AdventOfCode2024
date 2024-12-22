from copy import deepcopy
def WallCheck(Y, X, Make):
    global GlitchWalls
    global TempGrid
    global Direction
    global DirectionIndex
    for i in range(4):
        if Make:
            if 0 <= Y + (2*DirectionIndex[i][0]) < len(Race)  and 0 <= X + (2*DirectionIndex[i][1]) < len(Race[0])  and Race[Y + DirectionIndex[i][0]][X + DirectionIndex[i][1]] == '#' and Race[Y + (2*DirectionIndex[i][0])][X + (2*DirectionIndex[i][1])] != "#" and (Y + DirectionIndex[i][0], X + DirectionIndex[i][1]) not in GlitchWalls:
                GlitchWalls.append((Y + DirectionIndex[i][0], X + DirectionIndex[i][1]))  
        else:
            if TempGrid[Y + DirectionIndex[i][0]][X + DirectionIndex[i][1]] == '|':
                return Y + (2*DirectionIndex[i][0]), X + (2*DirectionIndex[i][1])
    return None

def StepMaker(Wallcheck):
    global Yindex
    global Xindex
    global Race
    global Direction
    global DirectionIndex
    global Steps
    global GlitchWalls
    while Race[Yindex][Xindex] != "E":
        if Wallcheck:
            WallCheck(Yindex, Xindex, True)
        Steps.append((Yindex, Xindex))
        while Race[Yindex + DirectionIndex[Direction][0]][Xindex + DirectionIndex[Direction][1]] == '#' or (Yindex + DirectionIndex[Direction][0], Xindex + DirectionIndex[Direction][1]) in Steps:
            Direction = (Direction+1)%4
        Yindex += DirectionIndex[Direction][0]
        Xindex += DirectionIndex[Direction][1]
        # print(len(Steps), Yindex, Xindex)
    Steps.append((Yindex, Xindex)) #Just adding the End node, because it isn't included in the loop

def P1():
    global Yindex
    global Xindex
    global Steps
    global total
    global Race
    global TempGrid
    global Direction
    global GlitchWalls
    StepMaker(True)
    Xindex = FXindex
    Yindex = FYindex
    Direction = 2
    Past = []
    for i in range(len(GlitchWalls)):
        # breakpoint()
        TempGrid = deepcopy(Race)
        TempGrid[GlitchWalls[i][0]][GlitchWalls[i][1]] = "|"
        while True:
            Glitch = WallCheck(Yindex, Xindex, False)
            if Glitch != None:
                NYindex, NXindex = Glitch
                if Steps.index((NYindex, NXindex)) - Steps.index((Yindex, Xindex)) >= 102:
                    total += 1
                    print(total)
                break
            Past.append((Yindex, Xindex))
            while TempGrid[Yindex + DirectionIndex[Direction][0]][Xindex + DirectionIndex[Direction][1]] == '#' or (Yindex + DirectionIndex[Direction][0], Xindex + DirectionIndex[Direction][1]) in Past:
                Direction = (Direction+1)%4
            Yindex += DirectionIndex[Direction][0]
            Xindex += DirectionIndex[Direction][1]
        # for i in TempGrid:
        #     print(i)
        # print()

def P2():
    global Yindex
    global Xindex
    global Race
    global Direction
    global DirectionIndex
    global Steps
    global GlitchWalls
    global total
    StepMaker(False)
    # breakpoint()
    for i in range(len(Steps)):
        for j in range(41):
            for k in range(41):
                if 0 <= Steps[i][0] + (j - 20) < len(Race) and 0 <= Steps[i][1] + (k - 20) < len(Race[0]) and abs(k-20)+abs(j - 20) <= 20 and Race[Steps[i][0] + (j - 20)][Steps[i][1] + (k - 20)] != "#" and Steps.index((Steps[i][0] + (j - 20), Steps[i][1] + (k - 20))) - Steps.index((Steps[i][0], Steps[i][1])) >= 100 + abs(j-20) + abs(k - 20):
                    total += 1
        print(i)


with open("input20.txt", "r") as f:
    DirectionIndex = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    Direction = 2
    GlitchWalls = []
    Race = f.readlines()
    Race = list(map(lambda x: list(x.replace("\n", "")), Race))
    Steps = []
    FXindex = -29
    FYindex = -29
    for i in range(len(Race)):
        if "S" in Race[i]:
            FXindex = Race[i].index("S")
            FYindex = i
            break

    total = 0
    Xindex = FXindex
    Yindex = FYindex
    Direction = 2
    # P1()
    P2()
    print(total)










