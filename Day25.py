# MERRY CHRISTMAS!

def SchemToVal(Grid):
    global Keys
    global Locks
    Val = [0 for e in range(len(Grid[0]))]
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            if Grid[i][j] == "#":
                Val[j] += 1
    if Grid[0] == ".....":
        Keys.append(Val)
    elif Grid[-1] == ".....":
        Locks.append(Val)
    else:
        raise(ValueError)
    
def AddList(L1, L2):
    output = []
    for i in range(len(L1)):
        output.append(L1[i] + L2[i])
    return output

def CheckList(L1) -> bool:
    for j in L1:
        if j > HEIGHT:
            return False
    return True


with open("input25.txt", "r") as f:
    Schems = f.read().split("\n\n")
    Schems = list(map(lambda x: x.split("\n"), Schems))
    Keys = []
    Locks = []
    total = 0
    HEIGHT = len(Schems[0])
    WIDTH = len(Schems[0][0])
    for Schem in Schems:
        SchemToVal(Schem)
    print(Keys)
    print(Locks)
    for Key in Keys:
        for Lock in Locks:
            Combo = AddList(Key, Lock)
            if CheckList(Combo):
                total += 1
    print(total)

        
