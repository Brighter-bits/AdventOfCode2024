def follow(input, ArrayIndex, mIndex, direction) -> bool:
    try:
        match direction:
            case "TL":
                if input[ArrayIndex-2][mIndex-2] == "A" and input[ArrayIndex-3][mIndex-3] == "S":
                    print(direction)
                    return True
                else: return False
            case "TM":
                if input[ArrayIndex-2][mIndex] == "A" and input[ArrayIndex-3][mIndex] == "S":
                    print(direction)
                    return True
                else: return False
            case "TR":
                if input[ArrayIndex-2][mIndex+2] == "A" and input[ArrayIndex-3][mIndex+3] == "S":
                    print(direction)
                    return True
                else: return False
            case "ML":
                if input[ArrayIndex][mIndex-2] == "A" and input[ArrayIndex][mIndex-3] == "S":
                    print(direction)
                    return True
                else: return False
            case "MR":
                if input[ArrayIndex][mIndex+2] == "A" and input[ArrayIndex][mIndex+3] == "S":
                    print(direction)
                    return True
                else: return False
            case "BL":
                if input[ArrayIndex+2][mIndex-2] == "A" and input[ArrayIndex+3][mIndex-3] == "S":
                    print(direction)
                    return True
                else: return False
            case "BM":
                if input[ArrayIndex+2][mIndex] == "A" and input[ArrayIndex+3][mIndex] == "S":
                    print(direction)
                    return True
                else: return False
            case "BR":
                if input[ArrayIndex+2][mIndex+2] == "A" and input[ArrayIndex+3][mIndex+3] == "S":
                    print(direction)
                    return True
                else: return False
    except:
        return False

def X(input, ArrayIndex, mIndex) -> bool:
    try:
        if input[ArrayIndex-1][mIndex-1] == "M":
            if (input[ArrayIndex-1][mIndex+1] == "M" and input[ArrayIndex+1][mIndex-1] == "S" and input[ArrayIndex+1][mIndex+1] == "S") or (input[ArrayIndex+1][mIndex-1] == "M" and input[ArrayIndex-1][mIndex+1] == "S" and input[ArrayIndex+1][mIndex+1] == "S"):
                return True
        elif input[ArrayIndex+1][mIndex+1] == "M":
            if (input[ArrayIndex-1][mIndex+1] == "M" and input[ArrayIndex+1][mIndex-1] == "S" and input[ArrayIndex-1][mIndex-1] == "S") or (input[ArrayIndex+1][mIndex-1] == "M" and input[ArrayIndex-1][mIndex+1] == "S" and input[ArrayIndex-1][mIndex-1] == "S"):
                return True
        else:
            return False
    except:
        return False

def p1():
    with open("input4.txt", "r") as f:
        input = [[]]
        for i in range(140):
            input.append(list(f.readline()))
        input.pop(0)
        for i in range(len(input)):
            input[i] = [e for e in input[i] if e != "\n"]
            
        print(input[0])
        ArrayIndex = 0
        count = 0
        total = 0
        while True:
            try:
                mIndex = input[ArrayIndex].index("X", count)
                count = mIndex+1
                # print(mIndex)
                try:
                    if ArrayIndex-3 >= 0 and mIndex-3 >= 0:
                        if input[ArrayIndex-1][mIndex-1] == "M":
                            if follow(input, ArrayIndex, mIndex, "TL"):
                                total += 1
                except: pass

                try:
                    if ArrayIndex-3 >= 0 and mIndex >= 0:
                        if input[ArrayIndex-1][mIndex] == "M":
                            if follow(input, ArrayIndex, mIndex, "TM"):
                                total += 1
                except: pass

                try:
                    if ArrayIndex-3 >= 0 and mIndex+3 >= 0:
                        if input[ArrayIndex-1][mIndex+1] == "M":
                            if follow(input, ArrayIndex, mIndex, "TR"):
                                total += 1
                except: pass


                try:
                    if ArrayIndex >= 0 and mIndex-3 >= 0:
                        if input[ArrayIndex][mIndex-1] == "M":
                            if follow(input, ArrayIndex, mIndex, "ML"):
                                total += 1
                except: pass

                try:
                    if ArrayIndex >= 0 and mIndex+3 >= 0:
                        if input[ArrayIndex][mIndex+1] == "M":
                            if follow(input, ArrayIndex, mIndex, "MR"):
                                total += 1
                except: pass

                try:
                    if ArrayIndex+3 >= 0 and mIndex-3 >= 0:
                        if input[ArrayIndex+1][mIndex-1] == "M":
                            if follow(input, ArrayIndex, mIndex, "BL"):
                                total += 1
                except: pass

                try:
                    if ArrayIndex+1 >= 0 and mIndex >= 0:
                        if input[ArrayIndex+1][mIndex] == "M":
                            if follow(input, ArrayIndex, mIndex, "BM"):
                                total += 1
                except: pass

                try:
                    if ArrayIndex+1 >= 0 and mIndex+1 >= 0:
                        if input[ArrayIndex+1][mIndex+1] == "M":
                            if follow(input, ArrayIndex, mIndex, "BR"):
                                total += 1
                except: pass

            except Exception as e:
                print(e)
                if ArrayIndex == 140:
                    break
                else:
                    count = 0
                    ArrayIndex += 1
        print(total)


def p2():
    with open("input4.txt", "r") as f:
        input = [[]]
        for i in range(140):
            input.append(list(f.readline()))
        input.pop(0)
        for i in range(len(input)):
            input[i] = [e for e in input[i] if e != "\n"]
            
        print(input[0])
        ArrayIndex = 0
        count = 0
        total = 0
        while True:
            try:
                mIndex = input[ArrayIndex].index("A", count)
                count = mIndex+1
                try:
                    if ArrayIndex-1 >= 0 and mIndex-1 >= 0:
                        if X(input, ArrayIndex, mIndex):
                            total += 1
                except: pass


            except Exception as e:
                print(e)
                if ArrayIndex == 140:
                    break
                else:
                    count = 0
                    ArrayIndex += 1
    print(total)

p2()