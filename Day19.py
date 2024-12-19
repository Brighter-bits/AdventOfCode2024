def Check(string):
    global total   
    global Done
    # breakpoint()
    Valid = []
    for i in range(len(Towels)):
        if Towels[i] in string[:len(Towels[i])]:
            # print(string, Towels[i])
            # breakpoint()
            Valid.append(Towels[i])
    # print(Valid)
    for i in range(len(Valid)):
        if len(Valid[i]) == len(string):
            total += 1
            Done = True
            return True
    
    for i in range(len(Valid)):
        # breakpoint()
        if Check(string[len(Valid[i]):]):
            print(total)
            break
        if Done == True:
            return True
    

def Check2(string):
    global total
    # breakpoint()
    Valid = []
    Done = False
    for i in range(len(Towels)):
        if Towels[i] in string[:len(Towels[i])]:
            Valid.append(Towels[i])

    for i in range(len(Valid)):
        if not Done:
            if len(Valid[i]) == len(string):
                total += 1
                Done = True
                print(total)
            else:
                Check2(string[len(Valid[i]):])


with open("Example19.txt", "r") as f:
    Towels = sorted(f.readline().split(", "), key = lambda x: len(x), reverse = True)
    f.readline()
    Combos = f.readlines()
    print(len(Towels), len(Combos))
    Towels = list(map(lambda x: x.replace("\n", ""), Towels))
    Combos = list(map(lambda x: x.replace("\n", ""), Combos))
    print(Towels)
    print(Combos)
    total = 0
    for j in range(len(Combos)):
        # Possible = True
        # while Possible:
        #     if Combos[j] == "":
        #         print("HOORAY!")
        #         total += 1
        #         break
        #     Possible = False
        #     for i in range(len(Towels)):
        #         if Towels[i] in Combos[j][:len(Towels[i])]:
        #             print("Yay!")
        #             Combos[j] = Combos[j][len(Towels[i]):]
        #             Possible = True
        #             break
        Done = False
        print(Combos[j])
        Check2(Combos[j])
    # print(total)