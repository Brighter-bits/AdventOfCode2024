with open("input5.txt", "r") as f:
    switch = False
    Rules = []
    Lines = []
    for i in range(1371):
        input = f.readline()
        if input == "\n":
            switch = True
            continue
        if not switch:
            Rules.append(input)
        else:
            Lines.append(input)
    Rules = sorted(Rules)
    Rules = list(map(lambda x: x.replace("\n", "").split("|"), Rules))
    Lines = list(map(lambda x: x.replace("\n", "").split(","), Lines))
    RulesDict = {}
    for i in Rules:
        value = RulesDict.get(int(i[0]))
        if value == None:
            RulesDict[int(i[0])] = [int(i[1])]
        else:
            value.append(int(i[1]))
            RulesDict[int(i[0])] = value
    print(RulesDict)

    for Array in Lines:
        for i in range(len(Array)):
            