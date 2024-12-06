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
        FXindex = Xindex
        FYindex = Yindex
        Direction = 0 # 0 is forwards, 1 is right, 2 is down, 3 is left
        Step = 0
        for i in range(len(Area)):
            Area[i] = [e for e in Area[i] if e != "\n"]
        while 0 <= Xindex <= len(Area[0]) and 0 <= Yindex <= 129:
            match Direction:
                case 0:
                    if Area[Yindex][Xindex] != ".":
                        Area[Yindex][Xindex] += "U"
                    else:
                        Area[Yindex][Xindex] = "U"
                    
                    if Area[Yindex-1][Xindex] == "#":
                        Direction += 1
                    else:
                        Yindex -= 1

                case 1:
                    if Area[Yindex][Xindex] != ".":
                        Area[Yindex][Xindex] += "R"
                    else:
                        Area[Yindex][Xindex] = "R"
                    if Area[Yindex][Xindex+1] == '#':
                        Direction += 1
                    else:
                        Xindex += 1
                case 2:
                    if Area[Yindex][Xindex] != ".":
                        Area[Yindex][Xindex] += "D"
                    else:
                        Area[Yindex][Xindex] = "D"

                    if Area[Yindex+1][Xindex] == '#':
                        Direction += 1
                    else:
                        Yindex += 1
                case 3:
                    if Area[Yindex][Xindex] != ".":
                        Area[Yindex][Xindex] += "L"
                    else:
                        Area[Yindex][Xindex] = "L"

                    if Area[Yindex][Xindex-1] == '#':
                        Direction = 0
                    else:
                        Xindex -= 1
            Step += 1
        print("\n")
        for i in Area:
            print(i)
        print(Step)
        for i in range(Step):
            Xindex = FXindex
            Yindex = FYindex
            Place = list(Area)
            Test = 0
            Step2 = 0
            Continue = True
            Direction = 0
            while Continue and (0 <= Xindex <= len(Area[0]) and 0 <= Yindex <= 129):
                match Direction:
                    case 0:
                        if Test == 2 and ("U" in Place[Yindex][Xindex]):
                            loop += 1
                            Continue = False
                        if Place[Yindex][Xindex] != ".":
                            Place[Yindex][Xindex] += "U"
                        else:
                            Place[Yindex][Xindex] = "U"
                        
                        if Test == 1:
                            Test += 1
                        if Step2 == i:
                            try:
                                Place[Yindex-1][Xindex] = "#"
                            except:
                                Continue = False
                            Test +=1

                        try:
                            if Place[Yindex-1][Xindex] == "#":
                                Direction += 1
                            else:
                                Yindex -= 1
                        except:
                            Continue = False



                    case 1:
                        if Test == 2 and ("R" in Place[Yindex][Xindex]):
                            loop += 1
                            Continue = False
                        if Place[Yindex][Xindex] != ".":
                            Place[Yindex][Xindex] += "R"
                        else:
                            Place[Yindex][Xindex] = "R"

                        if Test == 1:
                            Test += 1

                        if Step2 == i:
                            try:
                                Place[Yindex][Xindex+1] = "#"
                            except:
                                Continue = False
                            Test += 1

                        try:
                            if Place[Yindex][Xindex+1] == '#':
                                Direction += 1
                            else:
                                Xindex += 1
                        except:
                            Continue = False



                    case 2:
                        if Test == 2 and ("D" in Place[Yindex][Xindex]):
                            loop += 1
                            Continue = False
                        if Place[Yindex][Xindex] != ".":
                            Place[Yindex][Xindex] += "D"
                        else:
                            Place[Yindex][Xindex] = "D"

                        if Test == 1:
                            Test += 1

                        if Step2 == i:
                            try:
                                Place[Yindex+1][Xindex] = "#"
                            except:
                                Continue = False
                            Test += 1

                        try:
                            if Place[Yindex+1][Xindex] == '#':
                                Direction += 1
                            else:
                                Yindex += 1
                        except:
                            Continue = False

      
                    
                    case 3:
                        if Test == 2 and ("L" in Place[Yindex][Xindex]):
                            loop += 1
                            Continue = False
                        if Place[Yindex][Xindex] != ".":
                            Place[Yindex][Xindex] += "L"
                        else:
                            Place[Yindex][Xindex] = "L"

                        if Test == 1:
                            Test += 1

                        if Step2 == i:
                            try:
                                Place[Yindex][Xindex-1] = "#"
                            except:
                                Continue = False
                            Test += 1

                        try:
                            if Place[Yindex][Xindex-1] == '#':
                                Direction = 0
                            else:
                                Xindex -= 1
                        except:
                            Continue = False


                Step2 += 1
            print("Complete", i)
        print(loop)

p2()