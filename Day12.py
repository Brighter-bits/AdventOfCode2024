def Food(Y, X, Target): #It's supposed to say flood
    global Banned
    global Visited   
    global Edges 
    try:
        if Y < 0 or X < 0 or X > len(Fields[0])-1 or Y > len(Fields)-1:
            Edges += 1
        elif [Y, X] in Banned or Fields[Y][X] != Target:
            Edges += 1
        elif [Y, X] in Visited:
            pass
        else:
            Visited.append([Y, X])
            Food(Y-1, X, Target)
            Food(Y, X+1, Target)
            Food(Y+1, X, Target)
            Food(Y, X-1, Target)
    except:
        pass
        
def DropFood(Y, X, Target, Direction, Field):
    global Banned
    global Visited   
    global Edges 
    global Fields
    global StreakDirection
    # breakpoint()
    try:
        if Y < 0 or X < 0 or X > len(Fields[0])-1 or Y > len(Fields)-1:
            match Direction:
                case "u":
                    Fields[Y+1][X] += "u" + str(Field)
                case "r":
                    Fields[Y][X-1] += "r" + str(Field)
                case "d":
                    Fields[Y-1][X] += "d" + str(Field)
                case "l":
                    Fields[Y][X+1] += "l" + str(Field)
        elif [Y, X] in Banned or Target not in Fields[Y][X]:
            match Direction:
                case "u":
                    Fields[Y+1][X] += "u" + str(Field)
                case "r":
                    Fields[Y][X-1] += "r" + str(Field)
                case "d":
                    Fields[Y-1][X] += "d" + str(Field)
                case "l":
                    Fields[Y][X+1] += "l" + str(Field)
        elif [Y, X] in Visited:
            pass
        else:
            Visited.append([Y, X])
            Fields[Y][X] += str(Field)
            DropFood(Y-1, X, Target, "u", Field)
            DropFood(Y, X+1, Target, "r", Field)
            DropFood(Y, X-1, Target, "l", Field)
            DropFood(Y+1, X, Target, "d", Field)
    except Exception as e:
        print(e)
        
def SearchLine(Y, Target, Field):
    global Banned
    Side = 0
    for Direction in range(2):
        for Line in range(len(Fields)):
            Touch = False
            for i in range(len(Fields[Line])):
                # if Target == "E":
                #     breakpoint()
                if Target in Fields[Line][i] and str(Field) in Fields[Line][i]:
                    if [Line, i] not in Banned:
                        Banned.append([Line, i])
                    if Directions[Direction] in Fields[Line][i]:
                        Touch = True
                    else:
                        if Touch == True:
                            Side += 1
                        Touch = False
                else:
                    if Touch == True:
                        Side += 1
                    Touch = False
            if Touch == True:
                Side += 1

    return Side

def SearchColumn(X, Target, Field):
    global Banned
    Side = 0
    for Direction in range(2, 4):
        for column in range(len(Fields)):
            Touch = False
            for i in range(len(Fields)):
                # if [i, column] == [0, 0] and Direction == 3:
                #     breakpoint()
                if Target in Fields[i][column] and str(Field) in Fields[i][column]:
                    if [i, column] not in Banned:
                        Banned.append([i, column])
                    if Directions[Direction] in Fields[i][column]:
                        Touch = True
                    else:
                        if Touch == True:
                            Side += 1
                        Touch = False
                else:
                    if Touch == True:
                        Side += 1
                    Touch = False
            if Touch == True:
                Side += 1
    return Side


with open("input12.txt", "r") as f:
    Fields = f.readlines()
    Fields = list(map(lambda x: list(x), Fields))
    for i in range(len(Fields)):
        Fields[i].remove("\n")
    Banned = []
    Geometry = []
    Targets = []
    for Y in range(len(Fields)):
        for X in range(len(Fields[0])):
            if [Y, X] not in Banned:
                StreakDirection = ""
                Visited = []
                Edges = 0
                if Fields[Y][X] not in Targets:
                    Targets.append(Fields[Y][X])
                DropFood(Y, X, Fields[Y][X], "", [Y, X])
                Banned.extend(Visited)
                Geometry.append(["", len(Visited)])
                # breakpoint()
    Banned = []
    Directions = ["u", "d", "l", "r"]
    count = 0
    for i in range(len(Fields)):
        print(Fields[i])
    for Y in range(len(Fields)):
        for X in range(len(Fields[0])):
            Objective = ""
            if [Y, X] not in Banned:
                print(Y, X)
                Edges = 0
                for Letters in Targets:
                    if Letters in Fields[Y][X]:
                        Objective = Letters

                Line = -1
                Line = SearchLine(Y, Objective, [Y, X])
                print(Line)
                Edges += Line

                Line = -1
                Line = SearchColumn(X, Objective, [Y, X])
                # print(Line)
                Edges += Line
                print(Edges)

                Geometry[count][0] = Edges
                count += 1
                
                    

                    

    print(Geometry)
    total = 0
    # print(Targets)
    # for i in range(len(Fields)):
    #     print(Fields[i])
    for i in range(len(Geometry)):
        total += Geometry[i][0] * Geometry[i][1]
    print(total)

