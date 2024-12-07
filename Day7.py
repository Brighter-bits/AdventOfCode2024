
Calc = lambda x, y, z: x*y if z == "1" else (int(str(x) + str(y)) if z == "2" else x+y) # If True Add, else Mult

Part = 2

with open("input7.txt", "r") as f:
    LineNumber = 850
    Targets = []
    Numbers = []
    for i in range (LineNumber):
        Targets.append(None)
        Numbers.append(None)

    for i in range(LineNumber):
        Targets[i], Numbers[i] = f.readline().split(":")


    Targets = list(map(int, Targets))

    Numbers = list(map(lambda x: x.replace("\n", "").split(), Numbers))
    for i in range(len(Numbers)):
        Numbers[i] = list(map(int, Numbers[i]))
    Valid = 0
    for i in range(LineNumber):
        print(i+1)
        if Part == 1:
            Mask = "0b"
        else:
            Mask = ""
        for j in range(len(Numbers[i])-1):
            Mask += "0"
        total = 0
        if Part == 1:
            while total != Targets[i]:
                total = 0
                # print(len(Mask[2:]), Mask[2:], len(Numbers[i])-1)
                for j in range(len(Mask[2:])):
                    StripMask = list(Mask[2:])
                    if j == 0:
                        total = Calc(Numbers[i][0], Numbers[i][1], StripMask[j])
                        # print(StripMask, "start", len(StripMask), len(Numbers[i])-1)
                    else:
                        total = Calc(total, Numbers[i][j+1], StripMask[j])
                        # print(StripMask[j], j)
                Mask = format(int(Mask, 2)+1, ('#0'+str(len(Numbers[i])-1)+"b"))
                if len(Mask[2:]) > len(Numbers[i])-1:
                    break
                while len(Mask[2:]) < len(Numbers[i])-1:
                    Mask = Mask[:2] + "0" + Mask[2:]
        else:
            while total != Targets[i]:
                total = 0
                # print(len(Mask[2:]), Mask[2:], len(Numbers[i])-1)
                for j in range(len(Mask)):
                    StripMask = list(Mask)
                    if j == 0:
                        total = Calc(Numbers[i][0], Numbers[i][1], StripMask[j])
                        # print(StripMask, "start", len(StripMask), len(Numbers[i])-1)
                    else:
                        total = Calc(total, Numbers[i][j+1], StripMask[j])
                        # print(StripMask[j], j)
                Mask = int(Mask, 3) + 1
                digits = []
                while Mask:
                    digits.append(Mask % 3)
                    Mask = Mask // 3
                Mask = "".join(list(map(str, list(reversed(digits)))))
                if len(Mask) > len(Numbers[i])-1:
                    break
                while len(Mask) < len(Numbers[i])-1:
                    Mask = "0" + Mask
        if total == Targets[i]:
            Valid += total
    print(Valid)

