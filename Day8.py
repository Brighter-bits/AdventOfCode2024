def p1(Letters, Arrays):
    for i in range(len(Letters)):
        Locations = []
        for j in range(LIMIT):
            if Letters[i] in Arrays[i][j]:
                Locations.append((j, Arrays[i][j].index(Letters[i])))
        for j in range(len(Locations)):
            for k in range(len(Locations)):
                if j == k:
                    continue
                else:
                    VecY, VecX = Locations[j][0] - Locations[k][0], Locations[j][1] - Locations[k][1]
                    NewY, NewX = Locations[j][0] + VecY, Locations[j][1] + VecX
                    print(NewY, NewX, len(Arrays[i]))
                    if 0 <= NewY < LIMIT and 0 <= NewX < LIMIT:
                        Arrays[i][NewY][NewX] = "#"

def p2(Letters, Arrays):
    for i in range(len(Letters)):
        Locations = []
        for j in range(LIMIT):
            if Letters[i] in Arrays[i][j]:
                Locations.append((j, Arrays[i][j].index(Letters[i])))
        for j in range(len(Locations)):
            for k in range(len(Locations)):
                if j == k:
                    continue
                else:
                    print(Locations[j], Locations[k])
                    Arrays[i][Locations[j][0]][Locations[j][1]] = '#'
                    VecY, VecX = Locations[j][0] - Locations[k][0], Locations[j][1] - Locations[k][1]
                    multiplier = 1
                    while 0 <= (Locations[j][0] + (VecY*multiplier)) < LIMIT and 0 <= (Locations[j][1] + (VecX*multiplier)) < LIMIT:
                        NewY, NewX = (Locations[j][0] + (VecY*multiplier)), (Locations[j][1] + (VecX*multiplier))
                        Arrays[i][NewY][NewX] = "#"
                        multiplier += 1


with open("input8.txt", "r") as f:
    LIMIT = 50
    LetterFinder = [e for e in list(f.read()) if e != "\n" and e != "."]
    Letters = []
    for letter in LetterFinder:
        if letter not in Letters:
            Letters.append(letter)
    Arrays = [[] for a in range(len(Letters))]
    for i in range(len(Arrays)):
        f.seek(0)
        for j in range(LIMIT):
            Piece = [e if e == Letters[i] else "." for e in list(f.readline())]
            Arrays[i].append(Piece)

    # p1(Letters, Arrays)
    p2(Letters, Arrays)
    FinalArray = [['.' for b in range(LIMIT)] for a in range(LIMIT)]
    total = 0
    for Y in range(LIMIT):
        for X in range(LIMIT):
            for Layers in range(len(Letters)):
                if Arrays[Layers][Y][X] == "#":
                    FinalArray[Y][X] = "#"
                    total += 1
                    break
    for i in FinalArray:
        print(i)
    print(total)
    


