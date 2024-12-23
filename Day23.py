def P1(cons):
    valid = []
    for k in range(len(cons)):
        Target1 = cons[k][0]
        Target2 = cons[k][1]
        Target3 = []
        for i in range(len(cons)):
            for j in range(2):
                if j == 0 and (cons[i][j] == Target1 or cons[i][j] == Target2):
                    if cons[i][j+1] in Target3:
                        valid.append((Target1, Target2, cons[i][j+1]))
                    else:
                        Target3.append(cons[i][j+1])
                elif (cons[i][j] == Target1 or cons[i][j] == Target2):
                    if cons[i][j-1] in Target3:
                        valid.append((Target1, Target2, cons[i][j-1]))
                    else:
                        Target3.append(cons[i][j-1])
    
    cache = []
    for element in valid:
        element = sorted(element)
        if element not in cache:
            cache.append(element)
    valid = list(cache)
    print(valid)
    print(len(valid))
    Possible = []
    for i in range(len(valid)):
        for j in range(3):
            if "t" in valid[i][j][0]:
                Possible.append(valid[i])
                break
    print(Possible)
    print(len(Possible))


def CheckDict(Key):
    global Links
    global cnet
    # breakpoint()
    if cnet == []:
        for i in range(len(Links[Key])):
            for Key2 in Links[Links[Key][i]]:
                if Key2 in Links[Key]:
                    cnet.append(Key2)
            if cnet != []:
                cnet.append(Key)
    else:
        cache = []
        # breakpoint()
        for i in cnet:
            for j in range(len(cnet)):
                if cnet[j] in Links[i] or cnet[j] == i:
                    cache.append(cnet[j])
            cnet = cache
            cache = []

def CheckCnet(net):
    global cnet
    cache = []
    cnet = net
    for i in cnet:
        for j in range(len(cnet)):
            if cnet[j] in Links[i] or cnet[j] == i:
                cache.append(cnet[j])
        cnet = cache
        cache = []




with open("input23.txt", "r") as f:
    cons = f.readlines()
    cons =  list(map(lambda x: x.replace("\n", "").split("-"), cons))
    comps = []
    for i in range(len(cons)):
        for j in range(2):
            if cons[i][j] not in comps:
                comps.append(cons[i][j])
    print(comps)
    print(cons)
    Pieces = []
    for i in range(len(cons)):
        cons[i] = sorted(cons[i])
    # P1(cons)

    Links = dict()
    for i in comps:
        Links[i] = []
    for Computer in cons:
        Links[Computer[0]].append(Computer[1])
        Links[Computer[1]].append(Computer[0])
    for Key in Links.keys():
        Links[Key] = sorted(Links[Key])
    # print(Links)
    nnet = []
    for Key in Links.keys():
        cnet = []
        CheckDict(Key)
        CheckDict(Key)
        Hold = []
        for element in cnet:
            if element not in Hold:
                Hold.append(element)
        cnet = Hold
        cnet = sorted(cnet)
        if cnet not in nnet:
            nnet.append(cnet)
    print(nnet)
    nnet = sorted(nnet, key=lambda x: len(x), reverse=True)
    Password = ','.join(nnet[0])
    print(Password)
