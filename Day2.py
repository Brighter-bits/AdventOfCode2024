def p1():
    with open("input2.txt", "r") as f:
        input = f.readlines()
        input = list(map(lambda x: x.replace("\n", "").split(" "), input))
        for i in range(len(input)):
            input[i] = list(map(int, input[i]))
        Differences = []
        print(input)
        for i in range(len(input)):
            valid = True
            ArrayDiff = []
            for j in range(len(input[i])-1):
                ArrayDiff.append(input[i][j+1] - input[i][j])
            valid = True
            if 0 in ArrayDiff:
                valid = False
            for i in ArrayDiff:
                if valid:
                    if i < -3 or i > 3:
                        valid = False
            if ArrayDiff[0] > 0:
                for i in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[i] < 0:
                            valid = False
            else:
                for i in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[i] > 0:
                            valid = False


            if valid:
                Differences.append(ArrayDiff)

    print(Differences)
    print(len(Differences))

def p2():
    with open("input2.txt", "r") as f:
        input = f.readlines()
        input = list(map(lambda x: x.replace("\n", "").split(" "), input))
        for i in range(len(input)):
            input[i] = list(map(int, input[i]))
        Differences = []
        for i in range(len(input)):
            valid = True
            ArrayDiff = []
            for j in range(len(input[i])-1):
                ArrayDiff.append(input[i][j+1] - input[i][j])
            valid = True
            if 0 in ArrayDiff:
                valid = False
            for i in ArrayDiff:
                if valid:
                    if i < -3 or i > 3:
                        valid = False
            if ArrayDiff[0] > 0:
                for i in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[i] < 0:
                            valid = False
            else:
                for i in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[i] > 0:
                            valid = False


            if valid:
                Differences.append(ArrayDiff)
            else:
                for i in range(len(input[i])-1):
                    newinput = list(input[i])
                    newinput.pop(i)
                    valid = True
                    ArrayDiff = []
                    for j in range(len(newinput)-1):
                        ArrayDiff.append(newinput[j+1] - newinput[j])
                    valid = True
                    if 0 in ArrayDiff:
                        valid = False
                    for i in ArrayDiff:
                        if valid:
                            if i < -3 or i > 3:
                                valid = False
                    if ArrayDiff[0] > 0:
                        for i in range(0, len(ArrayDiff)):
                            if valid:
                                if ArrayDiff[i] < 0:
                                    valid = False
                    else:
                        for i in range(0, len(ArrayDiff)):
                            if valid:
                                if ArrayDiff[i] > 0:
                                    valid = False
                    if valid:
                        Differences.append(ArrayDiff)
                        break

    print(Differences)
    print(len(Differences))

p2()