def P1(Scrambled):
    UnScrambled = list(Scrambled)
    for i in range(len(UnScrambled)):
        try:
            Space = UnScrambled.index(".")
        except Exception as e:
            print(e)
            break
        
        value = -5

        while True:
            if UnScrambled[-1] == ".":
                UnScrambled.pop(-1)
            else:
                value = UnScrambled.pop(-1)
                UnScrambled[Space] = value
                break
    return UnScrambled

def P2(Scrambled):
    Gaps = {} # Tuple (Slots Remaining, Total Slots)
    UnScrambled = list(Scrambled)
    Space = 0
    while True:
        try:
            Space = UnScrambled.index(".", Space)
            count = 1
            while True:
                if UnScrambled[Space + count] == ".":
                    count += 1
                else:
                    break
            Gaps[Space] = [count, count]
            Space += count
        except Exception as e:
            print(e)
            break
    print(Gaps)
    
    pointer = -1
    while True:
        pointerAdd = -1
        Finding = True
        try:
            while Finding:
                if UnScrambled[pointer] == ".":
                    pointer -= 1
                else:
                    Instinct = UnScrambled[pointer] #ID
                    while True:
                        if UnScrambled[pointer + pointerAdd] == Instinct:
                            pointerAdd -= 1
                        else:
                            Finding = False
                            break
        
        except Exception as e:
            print(e)
            break
        # if Instinct == 2:
        #     breakpoint()
        Murder = Place = next((k for k, v in Gaps.items() if k >= len(UnScrambled)+pointer), None)
        if Murder != None:
            Gaps.pop(Murder)
        Place = next((k for k, v in Gaps.items() if v[0] >= -pointerAdd), None)
        if Place != None:
            index = Place + (Gaps[Place][1]-Gaps[Place][0])
            for i in range(-pointerAdd):
                try:
                    UnScrambled[index + i] = Instinct
                except:
                    breakpoint()
            Gaps[Place][0] = Gaps[Place][0] + pointerAdd
            for i in range(-pointerAdd):
                UnScrambled[pointer] = "."
                pointer -= 1
        else:
            pointer += pointerAdd
        # breakpoint()
    return UnScrambled






with open("input9.txt", "r") as f:
    input = list(map(int, list(f.read().replace("\n", ""))))
    Empty = False
    Scrambled = []
    for i in range(len(input)):
        if Empty:
            for j in range(input[i]):
                Scrambled.append(".")
        else:
            for j in range(input[i]):
                Scrambled.append(int(i/2))
        Empty = not Empty
    print(Scrambled)
    
    # UnScrambled = P1(Scrambled)
    UnScrambled2 = P2(Scrambled)
    total = 0
    print(UnScrambled2)
    Barrier = 0
    for i in range(len(UnScrambled2)):
        if UnScrambled2[i] != ".":
            total += (i-Barrier) * UnScrambled2[i]
        else:
            pass

    print(total)




