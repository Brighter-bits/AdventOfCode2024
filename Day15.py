import io
import os
import time
def Motion(CY, CX, New, NY, NX):
    global Map
    if Map[NY][NX] == ".":
        Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
        Map[NY] = Map[NY][:NX] + New + Map[NY][NX+1:]
    time.sleep(0.00000001)
    os.system('cls')
    for i in Map:
        print(i)

def Move(CY, CX, Direction) -> bool:
    # breakpoint()
    global Map
    global Xindex
    global Yindex
    global buffer
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
                buffer.writelines(f'Motion({CY}, {CX}, "O", {NY}, {NX});')
                # Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                # Map[NY] = Map[NY][:NX] + "O" + Map[NY][NX+1:]
                return True
        case '.':
            return True
        case '@':
            if Move(NY, NX, Direction):
                buffer.seek(0)
                exec(buffer.read())
                Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                Map[NY] = Map[NY][:NX] + "@" + Map[NY][NX+1:]
                Xindex = NX
                Yindex = NY
        case '[':
            if NX == CX:
                if Move(NY, NX, Direction) and Move(NY, NX+1, Direction):
                    # Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    # Map[NY] = Map[NY][:NX] + "[" + Map[NY][NX+1:]
                    # Map[CY] = Map[CY][:CX+1] + "." + Map[CY][CX+2:]
                    # Map[NY] = Map[NY][:NX+1] + "]" + Map[NY][NX+2:]
                    buffer.writelines(f'Motion({CY}, {CX}, "[", {NY}, {NX});')
                    buffer.writelines(f'Motion({CY}, {CX+1}, "]", {NY}, {NX+1});')
                    return True
            else:
                if Move(NY, NX, Direction):
                    # Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    # Map[NY] = Map[NY][:NX] + "[" + Map[NY][NX+1:]
                    buffer.writelines(f'Motion({CY}, {CX}, "[", {NY}, {NX});')
                    return True

        case ']':
            if NX == CX:
                if Move(NY, NX, Direction) and Move(NY, NX-1, Direction):
                    # Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    # Map[NY] = Map[NY][:NX] + "]" + Map[NY][NX+1:]
                    # Map[CY] = Map[CY][:CX-1] + "." + Map[CY][CX:]
                    # Map[NY] = Map[NY][:NX-1] + "[" + Map[NY][NX:]
                    buffer.writelines(f'Motion({CY}, {CX}, "]", {NY}, {NX});')
                    buffer.writelines(f'Motion({CY}, {CX-1}, "[", {NY}, {NX-1});')
                    return True
            else:
                if Move(NY, NX, Direction):
                    # Map[CY] = Map[CY][:CX] + "." + Map[CY][CX+1:]
                    # Map[NY] = Map[NY][:NX] + "]" + Map[NY][NX+1:]
                    buffer.writelines(f'Motion({CY}, {CX}, "]", {NY}, {NX});')
                    return True

                

with open("input15.txt", "r") as f:
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


    buffer = io.StringIO() # I'm overcomplicating this
    for j in Map:
        print(j)
    for i in range(len(Orders)):
        Move(Yindex, Xindex, Orders[i])
        # time.sleep(0.001)
        # os.system('cls')
        # for j in Map:
        #     print(j)
        buffer.seek(0)
        buffer.truncate()
    
    
        
    total = 0
    count = 0
    for Y in range(len(Map)):
        for X in range(len(Map[0])):
            if Map[Y][X] == '[' or Map[Y][X] == 'O':
                total += ((100)*(Y)) + (X)
                count += 1
    print(total, count)