import math
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
    for i in range(len(Lines)):
        Lines[i] = list(map(int, Lines[i]))
    RulesDict = {}
    for i in Rules:
        value = RulesDict.get(int(i[0]))
        if value == None:
            RulesDict[int(i[0])] = [int(i[1])]
        else:
            value.append(int(i[1]))
            RulesDict[int(i[0])] = value
    print(RulesDict)
    Correct = []
    Incorrect = []
    for Array in Lines: # For every single Array in the total number
        Valid = True
        for i in range(len(Array)): # Iterate over each part of the array
            for j in RulesDict[Array[i]]: # Get the incorrect ones and then look backwards
                if j in Array[0:i]:
                    Valid = False
                    break
        if Valid:
            Correct.append(Array[math.floor(len(Array)/2)])
        else:
            Incorrect.append(Array)
    mIncorrect = []
    for Array in Incorrect:
        count = 0
        while True:
            try:
                for j in RulesDict[Array[count]]:
                    if j in Array[0:count]:
                        buffer = Array[count]
                        Array[count] = Array[count-1]
                        Array[count-1] = buffer
                        count = 0
                        continue
                count += 1
            except:
                break
        mIncorrect.append(Array[math.floor(len(Array)/2)])

    print(Correct)
    print(sum(Correct))
    print(Incorrect)
    print(sum(mIncorrect))
