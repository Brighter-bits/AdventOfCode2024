import subprocess
def Move(CY, CX, Direction, Boxed = False) -> bool:
    global Map
    global Xindex
    global Yindex
    NY = CY
    NX = CX
    match Direction:
        case '^':
            NY -= 1
        case '>':
            NX += 1
        case '<':
            NX -= 1
        case 'v':
            NY += 1

    match Map[CY][CX]:
        case '#':
            return False
        case 'O':
            if Move(NY, NX, Direction):
                Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                Map[NY] = Map[NY][:NX] + "O" + Map[NY][NX+1:]
                return True
        case '.':
            return True
        case '@':
            if Move(NY, NX, Direction):
                Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                Map[NY] = Map[NY][:NX] + "@" + Map[NY][NX+1:]
                Xindex = NX
                Yindex = NY
        case '[':
            if NX == CX:
                if Move(NY, NX, Direction) and (Boxed or Move(NY, NX+1, Direction, True)):
                    Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    Map[NY] = Map[NY][:NX] + "[" + Map[NY][NX+1:]
                    Map[CY] = Map[CY][:CX+1] + "." + Map[CY][CX+2:]
                    Map[NY] = Map[NY][:NX+1] + "]" + Map[NY][NX+2:]
                    return True
            else:
                if Move(NY, NX, Direction):
                    Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    Map[NY] = Map[NY][:NX] + "[" + Map[NY][NX+1:]
                    return True

        case ']':
            if NX == CX:
                if Move(NY, NX, Direction) and (Boxed or Move(NY, NX-1, Direction, True)):
                    Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    Map[NY] = Map[NY][:NX] + "]" + Map[NY][NX+1:]
                    Map[CY] = Map[CY][:CX-1] + "." + Map[CY][CX:]
                    Map[NY] = Map[NY][:NX-1] + "[" + Map[NY][NX:]
                    return True
            else:
                if Move(NY, NX, Direction):
                    Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    Map[NY] = Map[NY][:NX] + "]" + Map[NY][NX+1:]
                    return True

                

with open("Example15.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")
    Map = input[0].split("\n")
    Orders = input[1].replace("\n", "")
    NewMap = []
    Part2 = True
    if Part2:
        for i in range(len(Map)):
            NewMap.append(Map[i].replace("#", "##").replace(".", "..").replace("O", '[]').replace("@", "@."))
        Map = NewMap

    for i in range(len(Map)):
        if "@" in Map[i]:
            Xindex = Map[i].index("@")
            Yindex = i
            break


    for i in range(len(Orders)):
        Move(Yindex, Xindex, Orders[i])
        for j in Map:
            print(j)
    
    
        
    total = 0
    count = 0
    for Y in range(len(Map)):
        for X in range(len(Map[0])):
            if Map[Y][X] == '[' or Map[Y][X] == 'O':
                total += ((100)*(Y)) + (X)
                count += 1
    print(total, count)