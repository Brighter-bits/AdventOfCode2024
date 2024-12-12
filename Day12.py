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
        
def ProperFood(Y, X, Target, Direction):
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
            Food(Y-1, X, Target, "U")
            Food(Y, X+1, Target, "R")
            Food(Y+1, X, Target, "D")
            Food(Y, X-1, Target, "L")
    except:
        pass

with open("input12.txt", "r") as f:
    Fields = f.readlines()
    Fields = list(map(lambda x: list(x), Fields))
    for i in range(len(Fields)):
        Fields[i].remove("\n")
    Banned = []
    Geometry = []
    for Y in range(len(Fields)):
        for X in range(len(Fields[0])):
            if [Y, X] not in Banned:
                Visited = []
                Edges = 0
                Food(Y, X, Fields[Y][X])
                Banned.extend(Visited)
                Geometry.append([Edges, len(Visited)])
                # breakpoint()
    print(Geometry)
    total = 0
    for i in range(len(Geometry)):
        total += Geometry[i][0] * Geometry[i][1]
    print(total)

