from functools import cache

@cache
def Check(string):
    global total   
    global Done
    # breakpoint()
    Valid = []
    if string == "":
        return True
    for i in range(len(Towels)):
        if Towels[i] in string[:len(Towels[i])]:
            # print(string, Towels[i])
            # breakpoint()
            Valid.append(Towels[i])
    # print(Valid)
    
    for i in range(len(Valid)):
        # breakpoint()
        if Check(string[len(Valid[i]):]):
            if Done != True:
                total += 1
                print(total)
                Done = True
            return True
    # global total   
    # global Done
    # # breakpoint()
    # Valid = []
    # for i in range(len(Towels)):
    #     if Towels[i] in string[:len(Towels[i])]:
    #         # print(string, Towels[i])
    #         # breakpoint()
    #         Valid.append(Towels[i])
    # # print(Valid)
    # for i in range(len(Valid)):
    #     if len(Valid[i]) == len(string):
    #         total += 1
    #         Done = True
    #         return True                 ############### Old Code which didn't cache correcly
    
    # for i in range(len(Valid)):
    #     # breakpoint()
    #     if Check(string[len(Valid[i]):]):
    #         print(total)
    #         break
    #     if Done == True:
    #         return True






def HighCheck(Combo):
    global total
    @cache
    def Check2(string):
        global Bra
        CheckTotal = 0
        if Bra:
            # breakpoint()
            pass
        Valid = []
        if string == "":
            return 1

        for i in range(len(Towels)):
            if Towels[i] in string[:len(Towels[i])]:
                Valid.append(Towels[i])

        for i in range(len(Valid)):
            CheckTotal += Check2(string[len(Valid[i]):])
        return CheckTotal
    total += Check2(Combo)


with open("input19.txt", "r") as f:
    Towels = sorted(f.readline().split(", "), key = lambda x: len(x))
    f.readline()
    Combos = f.readlines()
    print(len(Towels), len(Combos))
    Towels = list(map(lambda x: x.replace("\n", ""), Towels))
    Combos = list(map(lambda x: x.replace("\n", ""), Combos))
    print(Towels)
    print(Combos)
    total = 0
    for j in range(len(Combos)):
        Done = False
        Bra = False
        if j == 2:
            Bra = True
        print(Combos[j])
        HighCheck(Combos[j])
    print(total)