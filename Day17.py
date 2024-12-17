def Combo(operand) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            raise(IndexError)
import math
def Run(Initial):
    global A
    global B
    global C
    A = Initial
    pointer = 0
    Outputs = []
    while pointer + 1 < len(instructions):
        operan = instructions[pointer+1]
        Jump = False
        match instructions[pointer]:
            case 0:
                A = math.floor(A/(2**Combo(operan)))
            case 1:
                B = B^operan
            case 2:
                B = Combo(operan)%8
            case 3:
                if A != 0:
                    Jump = True
                    pointer = operan
            case 4:
                B = B^C
            case 5:
                Outputs.append(Combo(operan)%8)
            case 6:
                B = math.floor(A/(2**Combo(operan)))
            case 7:
                C = math.floor(A/(2**Combo(operan)))
        if not Jump:
            pointer += 2
    Outputs = ','.join(str(i) for i in Outputs)
    return Outputs

def TASMAKER():
    global TA
    TAS = count
    for i in range(len(TA)):
        TAS -= (8**(i+1)*TA[-i-1])
    return TAS

def CountMaker():
    global TA
    temp = 0
    for i in range(len(TA)):
        # breakpoint()
        if i == 0:
            temp += (8*TA[-1-i])
        else:
            temp += ((8**(i))*7*TA[-1-i])
    print(temp)
    return temp


with open("input17.txt", "r") as f:
    FA = int(f.readline().replace("Register A: ", ""))
    FB = int(f.readline().replace("Register B: ", ""))
    FC = int(f.readline().replace("Register C: ", ""))
    f.readline()

    instructions = list(map(int, f.readline().replace("Program: ", "").split(",")))
    Target = ','.join(str(i) for i in instructions)
    count = 0
    increment = -1
    TA = []
    while increment > -len(Target):
        # A = FA
        B = FB
        C = FC
        out = Run(count)
        # print(out)

        if out == Target[increment:]:
            TA.append(TASMAKER())
            count = CountMaker()
            increment -= 2

        # if out == Target[-1]:
        #     TA.append(TASMAKER())
        #     count = (8*TA[0])
        #     print(count, CountMaker())
        #     # print(count, Target[-3:])
        #     # break

        # elif out == Target[-3:]:
        #     TA.append(TASMAKER())
        #     count = (8*TA[1]) + (64*(TA[0]))
        #     print(count, CountMaker())
        #     # print(count, Target[-5:])
        #     # break

        # elif out == Target[-5:]:
        #     TA.append(TASMAKER())
        #     print(CountMaker())
        #     count = (8*TA[2]) + (56*TA[1]) + ((8**2)*7*TA[0])
        #     print(count, Target[-7:], TA)

        # elif out == Target[-7:]:
        #     TA.append(TASMAKER())
        #     print(CountMaker())
        #     count = (8*TA[3]) + (56*TA[2]) + ((8**2)*7*TA[1]) + ((8**3)*7*TA[0])
        #     print(count, Target[-9:], TA)
        #     break

        else:
            count += 1
        # print(TA, count)

        # print(count)
    # print(count)