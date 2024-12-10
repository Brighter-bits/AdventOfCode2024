def Follow(Cy, Cx, Target):
    global total
    global input
    global Banned
    global Part
    print(Cy, Cx)
    if Part == 1:
        if (Cy + 1) < len(input) and input[Cy+1][Cx] == Target:
            if Target == 9 and [Cy+1, Cx] not in Banned:
                total += 1
                Banned.append([Cy+1, Cx])
                print("YAY")
            else:
                Follow(Cy+1, Cx, Target+1)
        if Cx + 1 < len(input[0]) and input[Cy][Cx+1] == Target:
            if Target == 9:
                total += 1
                Banned.append([Cy, Cx+1])
                print("YAY")
            else:
                Follow(Cy, Cx+1, Target+1)
        if Cy - 1 >= 0 and input[Cy-1][Cx] == Target:
            if Target == 9:
                total += 1
                Banned.append([Cy- 1, Cx])
                print("YAY")
            else:
                Follow(Cy-1, Cx, Target+1)
        if Cx - 1 >= 0 and input[Cy][Cx-1] == Target:
            if Target == 9:
                total += 1
                Banned.append([Cy, Cx - 1])
                print("YAY")
            else:
                Follow(Cy, Cx-1, Target+1)
    else:
        if (Cy + 1) < len(input) and input[Cy+1][Cx] == Target:
            if Target == 9:
                total += 1
                Banned.append([Cy+1, Cx])
                print("YAY")
            else:
                Follow(Cy+1, Cx, Target+1)
        if Cx + 1 < len(input[0]) and input[Cy][Cx+1] == Target:
            if Target == 9:
                total += 1
                Banned.append([Cy, Cx+1])
                print("YAY")
            else:
                Follow(Cy, Cx+1, Target+1)
        if Cy - 1 >= 0 and input[Cy-1][Cx] == Target:
            if Target == 9:
                total += 1
                Banned.append([Cy- 1, Cx])
                print("YAY")
            else:
                Follow(Cy-1, Cx, Target+1)
        if Cx - 1 >= 0 and input[Cy][Cx-1] == Target:
            if Target == 9:
                total += 1
                Banned.append([Cy, Cx - 1])
                print("YAY")
            else:
                Follow(Cy, Cx-1, Target+1)

def IncorrectDay():
    with open("input10.txt", "r") as f:
        inputb = f.read().replace("\n", ",").replace(" ", "").split(",")
        print(inputb)
        totalb = 0
        for words in inputb:
            Sum = 0
            letters = list(words)
            for j in letters:
                Sum += ord(j)
                Sum *= 17
                Sum %= 256
            totalb += Sum
        print(totalb)

with open("input10b.txt", "r") as f:
    total = 0
    Part = 2
    input = f.readlines()
    for i in range(len(input)):
        input[i] = list(input[i])
        input[i].pop(-1)
        input[i] = list(map(int, input[i]))
    print(input)
    for Cy in range(len(input)):
        for Cx in range(len(input[0])):
            Banned = []
            if input[Cy][Cx] == 0:
                Follow(Cy, Cx, 1)
                print("Done")
    print(total)