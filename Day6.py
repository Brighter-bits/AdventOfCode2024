from copy import deepcopy
def p1():
    with open("input6.txt", "r") as f:
        Area = f.readlines()
        Area = list(map(lambda x: list(x), Area))
        Xindex = -1
        Yindex = -1
        for i in range(130):
            if "^" in Area[i]:
                Xindex = Area[i].index("^")
                Yindex = i
                break
        loop = 0
        Direction = 0 # 0 is forwards, 1 is right, 2 is down, 3 is left
        while 0 <= Xindex <= len(Area[0]) and 0 <= Yindex <= 129:
            match Direction:
                case 0:
                    if Area[Yindex-1][Xindex] == "#":
                        Direction += 1
                    else:
                        Yindex -= 1
                case 1:
                    if Area[Yindex][Xindex+1] == '#':
                        Direction += 1
                    else:
                        Xindex += 1
                case 2:
                    if Area[Yindex+1][Xindex] == '#':
                        Direction += 1
                    else:
                        Yindex += 1
                case 3:
                    if Area[Yindex][Xindex-1] == '#':
                        Direction = 0
                    else:
                        Xindex -= 1
        total = list(map(lambda x: x.count("X"), Area))
        print(total)
        print(sum(total))
        print(loop)

def p2():
    with open("Input6.txt", "r") as f:
        Area = f.readlines()
        Area = list(map(lambda x: list(x), Area))
        Xindex = -1
        Yindex = -1
        for i in range(130):
            if "^" in Area[i]:
                Xindex = Area[i].index("^")
                Yindex = i
                break
        loop = 0
        FXindex = Xindex
        FYindex = Yindex
        Direction = 0 # 0 is forwards, 1 is right, 2 is down, 3 is left
        Steps = []
        for i in range(len(Area)):
            Area[i] = [e for e in Area[i] if e != "\n"]

        while 0 <= Xindex <= len(Area[0])-1 and 0 <= Yindex <= 129:
            Steps.append([Yindex, Xindex])
            match Direction:
                case 0:
                    try:
                        if Area[Yindex-1][Xindex] == "#":
                            Direction += 1
                        else:
                            Yindex -= 1
                    except:
                        break

                case 1:

                    try:
                        if Area[Yindex][Xindex+1] == '#':
                            Direction += 1
                        else:
                            Xindex += 1
                    except: break
                case 2:

                    try:
                        if Area[Yindex+1][Xindex] == '#':
                            Direction += 1
                        else:
                            Yindex += 1
                    except: break
                case 3:
                    try:
                        if Area[Yindex][Xindex-1] == '#':
                            Direction = 0
                        else:
                            Xindex -= 1
                    except: break
        print("\n")
        print(len(Steps))
        cache = Steps
        Steps = []
        for i in cache:
            if i not in Steps:
                Steps.append(i)
        print(len(Steps))
        for Coords in Steps:
            Xindex = FXindex
            Yindex = FYindex
            Place = deepcopy(Area)
            Continue = True
            Direction = 0
            if (Coords[0] == FYindex and Coords[1] == Xindex):
                Continue = False
            else:
                Place[Coords[0]][Coords[1]] = "#"
            if loop == 600:
                # breakpoint()
                pass
            while Continue and (0 <= Xindex <= len(Area[0])-1 and 0 <= Yindex <= 129):
                match Direction:
                    case 0:
                        if "U" in Place[Yindex][Xindex]:
                            loop += 1
                            Continue = False
                        Place[Yindex][Xindex] += "U"

                        try:
                            if Place[Yindex-1][Xindex] == "#":
                                Direction += 1
                        except:
                            Continue = False

                    case 1:
                        if "R" in Place[Yindex][Xindex]:
                            loop += 1
                            Continue = False
                        Place[Yindex][Xindex] += "R"

                        try:
                            if Place[Yindex][Xindex+1] == '#':
                                Direction += 1
                        except:
                            Continue = False

                    case 2:
                        if "D" in Place[Yindex][Xindex]:
                            loop += 1
                            Continue = False
                        Place[Yindex][Xindex] += "D"

                        try:
                            if Place[Yindex+1][Xindex] == '#':
                                Direction += 1
                        except:
                            Continue = False
                    
                    case 3:
                        if "L" in Place[Yindex][Xindex]:
                            loop += 1
                            Continue = False

                        Place[Yindex][Xindex] += "L"


                        try:
                            if Place[Yindex][Xindex-1] == '#':
                                Direction = 0
                        except:
                            Continue = False

                match Direction:
                    case 0:
                        Yindex -= 1
                    case 1:
                        Xindex += 1
                    case 2:
                        Yindex += 1
                    case 3:
                        Xindex -= 1

            
            # print("Complete", Coords, loop)
        print(loop)

p2()