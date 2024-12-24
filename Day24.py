# Christmas Eve!
from copy import deepcopy

def DictMaker(arr):
    WireDict = dict(arr[0])
    SwappableWires = dict(arr[1])
    WireDict = WireDict | SwappableWires
    return WireDict

def ComputeDict(SquishDict):
    total = 0
    for Key in SquishDict.keys():
        if "z" in Key:
            total += 1

    Valid = ["" for e in range(total)] 

    for Key in SquishDict.keys():
        if "z" in Key:
            Valid[int(Key[1:])] = SquishDict[Key]
    Num = ''.join(Valid)
    DenNum = int(Num, 2)
    return DenNum

def DictSquisher(WireDict):
    while True:
        Done = False
        for Key in WireDict.keys():
            if type(WireDict[Key]) == list:
                if (WireDict[Key][0] == "0" or WireDict[Key][0] == "1") and (WireDict[Key][2] == "0" or WireDict[Key][2] == "1"):
                    match WireDict[Key][1]:
                        case "AND":
                            if WireDict[Key][0] == "1" and WireDict[Key][2] == "1":
                                WireDict[Key] = "1"
                            else:
                                WireDict[Key] = "0"
                            
                        case "OR":
                            if WireDict[Key][0] == "1" or WireDict[Key][2] == "1":
                                WireDict[Key] = "1"
                            else:
                                WireDict[Key] = "0"
                        case "XOR":
                            if WireDict[Key][0] != WireDict[Key][2]:
                                WireDict[Key] = "1"
                            else:
                                WireDict[Key] = "0"
                    Done = True

                else:
                    # if WireDict[Key][0] == "x35":
                    #     breakpoint()
                    if WireDict[Key][0] != "0" and WireDict[Key][0] != "1" and (WireDict[WireDict[Key][0]] == "1" or WireDict[WireDict[Key][0]] == "0"):
                        WireDict[Key][0] = WireDict[WireDict[Key][0]]
                        Done = True
                    if WireDict[Key][2] != "0" and WireDict[Key][2] != "1" and (WireDict[WireDict[Key][2]] == "1" or WireDict[WireDict[Key][2]] == "0"):
                        WireDict[Key][2] = WireDict[WireDict[Key][2]]
                        Done = True
        
        if not Done:
            break
    return WireDict

def Binary(num):
    digits = []
    while num:
        digits.append(num % 2)
        num = num // 2
    num = "".join(list(map(str, list(reversed(digits)))))
    return num

def Test(num1, num2, Array):
    Answer = num1 + num2
    num1 = Binary(num1)
    num2 = Binary(num2)
    # breakpoint()
    for i in range(len(Array[0][:45])):
        try:
            Array[0][i][1] = num1[-i-1]
        except:
            Array[0][i][1] = "0"
    for i in range(len(Array[0][45:])):
        try:
            Array[0][i+45][1] = num2[-i-1]
        except:
            Array[0][i+45][1] = "0"
    Wires = DictMaker(Array)
    Wires = DictSquisher(Wires)
    try:
        if ComputeDict(Wires) == Answer:
            return True
        else:
            return False
    except:
        return False

def Order():
#     global input
    Wires = sorted(input[1], key=lambda x: (x[0], x[1][1]))
    for i in Wires:
        print(i)
        breakpoint()
#     import io
#     buffer = io.StringIO() # good thing I now know this
#     buffer.writelines('pycirc.Define("Day24");')
#     for i in range(45):
#         buffer.writelines(f'pycirc.Gate("x{i}", type="inp");')
#     for i in range(45):
#         buffer.writelines(f'pycirc.Gate("y{i}", type="inp");')
#     buffer.seek(0)
#     L.logic.
#     exec(buffer.read())

    

    


with open("input24.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")
    input = list(map(lambda x: x.split("\n"), input))
    input[1].pop(-1)
    Wires = {}
    # breakpoint()
    input[0] = list(map(lambda x: x.split(": "), input[0]))
    # breakpoint()
    input[1] = list(map(lambda x: x.split(" -> ")[::-1], input[1]))
    for i in range(len(input[1])):
        input[1][i][1] = input[1][i][1].split()
    # print(len(Wires))
    # breakpoint()
    # print(Test(50, 1000, input))
    #Brute Force time!
    indexes = []
    Order()

    # for pointer0 in range(len(input[1])):
    #     for pointer1 in range(len(input[1])):
    #         if pointer0 == pointer1:
    #             continue
    #         for pointer2 in range(len(input[1])):
    #             if pointer2 == pointer1 or pointer2 == pointer0:
    #                 continue
    #             for pointer3 in range(len(input[1])):
    #                 if pointer3 == pointer2 or pointer3 == pointer1 or pointer3 == pointer0:
    #                     continue
    #                 for pointer4 in range(len(input[1])):
    #                     if pointer4 == pointer3 or pointer4 == pointer2 or pointer4 == pointer1 or pointer4 == pointer0:
    #                         continue
    #                     for pointer5 in range(len(input[1])):
    #                         if pointer0 == pointer5 or pointer1 == pointer5 or pointer2 == pointer5 or pointer3 == pointer5 or pointer4 == pointer5:
    #                             continue
    #                         for pointer6 in range(len(input[1])):
    #                             if pointer6 == pointer0 or pointer6 == pointer1 or pointer6 == pointer2 or pointer6 == pointer3 or pointer6 == pointer4 or pointer6 == pointer5:
    #                                 continue
    #                             for pointer7 in range(len(input[1])):
    #                                 if pointer7 == pointer0 or pointer7 == pointer1 or pointer7 == pointer2 or pointer7 == pointer3 or pointer7 == pointer4 or pointer7 == pointer5 or pointer7 == pointer6:
    #                                     continue
    #                                 # breakpoint()
    #                                 Changeinput = deepcopy(input)          ################# I'll do it on paper
    #                                 cache = Changeinput[1][pointer0][0]
    #                                 Changeinput[1][pointer0][0] = Changeinput[1][pointer1][0]
    #                                 Changeinput[1][pointer1][0] = cache

    #                                 cache = Changeinput[1][pointer2][0]
    #                                 Changeinput[1][pointer2][0] = Changeinput[1][pointer3][0]
    #                                 Changeinput[1][pointer3][0] = cache

    #                                 cache = Changeinput[1][pointer4][0]
    #                                 Changeinput[1][pointer4][0] = Changeinput[1][pointer5][0]
    #                                 Changeinput[1][pointer5][0] = cache

    #                                 cache = Changeinput[1][pointer6][0]
    #                                 Changeinput[1][pointer6][0] = Changeinput[1][pointer7][0]
    #                                 Changeinput[1][pointer7][0] = cache

    #                                 output = Test(11, 13, Changeinput)
    #                                 if output:
    #                                     breakpoint()
    #                                 else:
    #                                     print(output)


