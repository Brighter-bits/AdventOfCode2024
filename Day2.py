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
            for j in ArrayDiff:
                if valid:
                    if j < -3 or j > 3:
                        valid = False
            if ArrayDiff[0] > 0:
                for j in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[j] < 0:
                            valid = False
            else:
                for j in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[j] > 0:
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
            for j in ArrayDiff:
                if valid:
                    if j < -3 or j > 3:
                        valid = False
            if ArrayDiff[0] > 0:
                for j in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[j] < 0:
                            valid = False
            else:
                for j in range(0, len(ArrayDiff)):
                    if valid:
                        if ArrayDiff[j] > 0:
                            valid = False


            if valid:
                Differences.append(ArrayDiff)
            else:
                print(input[i])
                for j in range(len(input[i])):
                    newinput = list(input[i])
                    newinput.pop(j)
                    print(newinput, j)
                    valid = True
                    ArrayDiff = []
                    for k in range(len(newinput)-1):
                        ArrayDiff.append(newinput[k+1] - newinput[k])
                    valid = True
                    if 0 in ArrayDiff:
                        valid = False
                    for k in ArrayDiff:
                        if valid:
                            if k < -3 or k > 3:
                                valid = False
                    if ArrayDiff[0] > 0:
                        for k in range(0, len(ArrayDiff)):
                            if valid:
                                if ArrayDiff[k] < 0:
                                    valid = False
                    else:
                        for k in range(0, len(ArrayDiff)):
                            if valid:
                                if ArrayDiff[k] > 0:
                                    valid = False
                    if valid:
                        Differences.append(ArrayDiff)
                        break

    # print(Differences)
    print(len(Differences))
# p1()
p2()