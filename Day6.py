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
        while 0 <= Xindex <= len(Area[0]) and 0 <= Yindex <= len(Area)-1:
            match Direction:
                case 0:
                    if Area[Yindex-1][Xindex] == "#":
                        Direction = (Direction+1)%4
                    else:
                        Yindex -= 1
                case 1:
                    if Area[Yindex][Xindex+1] == '#':
                        Direction = (Direction+1)%4
                    else:
                        Xindex += 1
                case 2:
                    if Area[Yindex+1][Xindex] == '#':
                        Direction = (Direction+1)%4
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
        DirectionIndex = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        Area = f.readlines()
        Area = list(map(lambda x: list(x.strip()), Area))
        Xindex = -1
        Yindex = -1
        for i in range(130):
            if "^" in Area[i]:
                Xindex = Area[i].index("^")
                Yindex = i
                break
        # loop = 0
        FXindex = Xindex
        FYindex = Yindex
        Direction = 0 # 0 is forwards, 1 is right, 2 is down, 3 is left
        # Steps = []
        for i in range(len(Area)):
            Area[i] = [e for e in Area[i] if e != "\n"]

        # while Xindex in range(len(Area[i])) and Yindex in range(len(Area)):
        #     Steps.append([Yindex, Xindex])
        #     match Direction:
        #         case 0:
        #             try:
        #                 if Area[Yindex-1][Xindex] == "#":
        #                     Direction = (Direction+1)%4
        #                 else:
        #                     Yindex -= 1
        #             except:
        #                 break

        #         case 1:

        #             try:
        #                 if Area[Yindex][Xindex+1] == '#':
        #                     Direction = (Direction+1)%4
        #                 else:
        #                     Xindex += 1
        #             except: break
        #         case 2:

        #             try:
        #                 if Area[Yindex+1][Xindex] == '#':
        #                     Direction = (Direction+1)%4
        #                 else:
        #                     Yindex += 1
        #             except: break
        #         case 3:
        #             try:
        #                 if Area[Yindex][Xindex-1] == '#':
        #                     Direction = (Direction+1)%4
        #                 else:
        #                     Xindex -= 1
        #             except: break
        # print("\n")
        # print(len(Steps))
        # cache = Steps
        # Steps = []
        # for i in cache:
        #     if i not in Steps:
        #         Steps.append(i)
        # print(len(Steps))
        loop = 0
        # for Coords in Steps:
        for theY in range(len(Area)):
            for theX in range(len(Area[0])):
                Xindex = FXindex
                Yindex = FYindex
                Previous = set()
                Continue = True
                Direction = 0
                LastNode = tuple()
                LastLastNode = tuple()
                # if (Coords[0] == FYindex and Coords[1] == FXindex):
                #     Continue = False
                # else:
                #     Area[Coords[0]][Coords[1]] = "#"
                if Area[theY][theX] == "#" or Area[theY][theX] == "^":
                    continue
                else:
                    Area[theY][theX] = '#'

                if loop == 6:
                    pass
                    # breakpoint()
                while Xindex in range(len(Area[0])) and Yindex in range(len(Area)) and (Direction, Yindex, Xindex) not in Previous:
                    match Direction:
                        case 0:
                            Previous.add((Direction, Yindex, Xindex))

                            # try:
                            #     if Area[Yindex-1][Xindex] == "#":
                            #         Direction = (Direction+1)%4
                            #         # LastLastNode = LastNode
                            #         # LastNode = [Yindex-1, Xindex]
                            # except Exception as e:
                            #     print(e)
                            #     Continue = False

                        case 1:
                            Previous.add((Direction, Yindex, Xindex))

                            # try:
                            #     if Area[Yindex][Xindex+1] == '#':
                            #         Direction = (Direction+1)%4
                            #         # LastLastNode = LastNode
                            #         # LastNode = [Yindex-1, Xindex]
                            # except Exception as e:
                            #     print(e)
                            #     Continue = False

                        case 2:
                            Previous.add((Direction, Yindex, Xindex))

                            # try:
                            #     if Area[Yindex+1][Xindex] == '#':
                            #         Direction = (Direction+1)%4
                            #         # LastLastNode = LastNode
                            #         # LastNode = [Yindex-1, Xindex]
                            # except Exception as e:
                            #     print(e)
                            #     Continue = False
                        
                        case 3:
                            Previous.add((Direction, Yindex, Xindex))

                            # try:
                            #     if Area[Yindex][Xindex-1] == '#':
                            #         Direction = 0
                            #         # LastLastNode = LastNode
                            #         # LastNode = [Yindex-1, Xindex]
                            # except Exception as e:
                            #     print(e)
                            #     Continue = False
                    try:
                        newY, newX = Yindex + DirectionIndex[Direction][0], Xindex + DirectionIndex[Direction][1]
                        if newY in range(len(Area)) and newX in range(len(Area[0])) and Area[newY][newX] == "#":
                            Direction = (Direction+1)%4
                        else:
                            Yindex = newY
                            Xindex = newX
                    except Exception as e:
                        print(e)
                        # Continue = False
                    # LastLastNode = LastNode
                    # LastNode = tuple([Yindex, Xindex])

                if (Direction, Yindex, Xindex) in Previous:
                    loop += 1
                    print(loop)
                    Continue = False
                # print("Complete", Coords, loop)
                # Area[Coords[0]][Coords[1]] = "."
                Area[theY][theX] = "."
        print(loop)

p2()