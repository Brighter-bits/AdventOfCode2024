from functools import cache
from collections import Counter
@cache
def LastRobot(Start, End):
    match Start:
        case "0":
            match End:
                case "0":
                    return ["A"]
                case "1":
                    return ["^<A"]
                case "2":
                    return ["^A"]
                case "3":
                    return ["^>A", ">^A"]
                case "4":
                    return ["^^<A"]
                case "5":
                    return ["^^A"]
                case "6":
                    return ["^^>A", ">^^A"]
                case "7":
                    return ["^^^<A"]
                case "8":
                    return ["^^^A"]
                case "9":
                    return ["^^^>A", ">^^^A"]
                case "A":
                    return [">A"]
        case "1":
            match End:
                case "0":
                    return [">vA"]
                case "1":
                    return ["A"]
                case "2":
                    return [">A"]
                case "3":
                    return [">>A"]
                case "4":
                    return ["^A"]
                case "5":
                    return ["^>A", ">^"]
                case "6":
                    return ["^>>A", ">>^A"]
                case "7":
                    return ["^^A"]
                case "8":
                    return ["^^>A", ">^^A"]
                case "9":
                    return ["^^>>A", ">>^^A"]
                case "A":
                    return [">>vA"]
        case "2":
            match End:
                case "0":
                    return ["vA"]
                case "1":
                    return ["<A"]
                case "2":
                    return ["A"]
                case "3":
                    return [">A"]
                case "4":
                    return ["<^A", "^<A"]
                case "5":
                    return ["^A"]
                case "6":
                    return ["^>A", ">^A"]
                case "7":
                    return ["<^^A", "^^<A"]
                case "8":
                    return ["^^A"]
                case "9":
                    return ["^^>A", ">^^A"]
                case "A":
                    return [">vA", "v>A"]
        case "3":
            match End:
                case "0":
                    return ["<vA", "v<A"]
                case "1":
                    return ["<<A"]
                case "2":
                    return ["<A"]
                case "3":
                    return ["A"]
                case "4":
                    return ["<<^A", "^<<A"]
                case "5":
                    return ["<^A", "^<A"]
                case "6":
                    return ["^A"]
                case "7":
                    return ["<<^^A", "^^<<A"]
                case "8":
                    return ["<^^A", "^^<A"]
                case "9":
                    return ["^^A"]
                case "A":
                    return ["vA"]
        case "4":
            match End:
                case "0":
                    return [">vvA"]
                case "1":
                    return ["vA"]
                case "2":
                    return [">vA", "v>A"]
                case "3":
                    return [">>vA", "v>>A"]
                case "4":
                    return ["A"]
                case "5":
                    return [">A"]
                case "6":
                    return [">>A"]
                case "7":
                    return ["^A"]
                case "8":
                    return ["^>A", ">^A"]
                case "9":
                    return ["^>>A", ">>^A"]
                case "A":
                    return [">>vvA"]
        case "5":
            match End:
                case "0":
                    return ["vvA"]
                case "1":
                    return ["<vA", "v<A"]
                case "2":
                    return ["vA"]
                case "3":
                    return ["v>A", ">vA"]
                case "4":
                    return ["<A"]
                case "5":
                    return ["A"]
                case "6":
                    return [">A"]
                case "7":
                    return ["<^A", "^<A"]
                case "8":
                    return ["^A"]
                case "9":
                    return [">^A", "^>A"]
                case "A":
                    return ["vv>A", ">vvA"]
        case "6":
            match End:
                case "0":
                    return ["<vvA", "vv<A"]
                case "1":
                    return ["<<vA", "v<<A"]
                case "2":
                    return ["<vA", "v<A"]
                case "3":
                    return ["vA"]
                case "4":
                    return ["<<A"]
                case "5":
                    return ["<A"]
                case "6":
                    return ["A"]
                case "7":
                    return[ "<<^A", "^<<A"]
                case "8":
                    return ["<^A", "^<A"]
                case "9":
                    return ["^A"]
                case "A":
                    return ["vvA"]
        case "7":
            match End:
                case "0":
                    return [">vvvA"]
                case "1":
                    return ["vvA"]
                case "2":
                    return ["vv>A", ">vvA"]
                case "3":
                    return ["vv>>A", ">>vvA"]
                case "4":
                    return ["vA"]
                case "5":
                    return [">vA", "v>A"]
                case "6":
                    return [">>vA", "v>>A"]
                case "7":
                    return ["A"]
                case "8":
                    return [">A"]
                case "9":
                    return [">>A"]
                case "A":
                    return [">>vvvA"]
        case "8":
            match End:
                case "0":
                    return ["vvvA"]
                case "1":
                    return ["<vvA", "vv<A"]
                case "2":
                    return ["vvA"]
                case "3":
                    return ["vv>A", ">vvA"]
                case "4":
                    return ["<vA", "v<A"]
                case "5":
                    return ["vA"]
                case "6":
                    return ["v>A", ">vA"]
                case "7":
                    return ["<A"]
                case "8":
                    return ["A"]
                case "9":
                    return [">A"]
                case "A":
                    return ["vvv>A", ">vvvA"]
        case "9":
            match End:
                case "0":
                    return ["<vvvA", "vvv<A"]
                case "1":
                    return ["<<vvA", "vv<<A"]
                case "2":
                    return ["<vvA", "vv<A"]
                case "3":
                    return ["vvA"]
                case "4":
                    return ["<<vA", "v<<A"]
                case "5":
                    return ["<vA", "v<A"]
                case "6":
                    return ["vA"]
                case "7":
                    return ["<<A"]
                case "8":
                    return ["<A"]
                case "9":
                    return ["A"]
                case "A":
                    return ["vvvA"]
        case "A":
            match End:
                case "0":
                    return ["<A"]
                case "1":
                    return ["^<<A"]
                case "2":
                    return ["<^A", "^<A"]
                case "3":
                    return ["^A"]
                case "4":
                    return ["^^<<A"]
                case "5":
                    return ["<^^A", "^^<A"]
                case "6":
                    return ["^^A"]
                case "7":
                    return ["^^^<<A"]
                case "8":
                    return ["<^^^A", "^^^<A"]
                case "9":
                    return ["^^^A"]
                case "A":
                    return ["A"]

@cache
def DirectionRobo(Start, End):
    match Start:
        case "A":
            match End:
                case "A":
                    return "A"
                case "^":
                    return "<A"
                case ">":
                    return "vA"
                case "v":
                    return "<vA"
                case "<":
                    return "v<<A"
        case "^":
            match End:
                case "A":
                    return ">A"
                case "^":
                    return "A"
                case "v":
                    return "vA"
                case ">":
                    return "v>A"
                case "<":
                    return "v<A"
        case ">":
            match End:
                case "A":
                    return "^A"
                case ">":
                    return "A"
                case "v":
                    return "<A"
                case "^":
                    return "<^A"
                case "<":
                    return "<<A"
        case "v":
            match End:
                case ">":
                    return ">A"
                case "v":
                    return "A"
                case "^":
                    return "^A"
                case "<":
                    return "<A"
                case "A":
                    return "^>A"
        case "<":
            match End:
                case "<":
                    return "A"
                case "v":
                    return ">A"
                case ">":
                    return ">>A"
                case "^":
                    return ">^A"
                case "A":
                    return ">>^A"

@cache
def Robots(input):
    if input == "A":
        return "A"
    input = "A" + input
    output = ""
    for i in range(len(input)-1):
        output += DirectionRobo(input[i], input[i+1])
    
    return output

    

def Solve(Code: str):
    nums = ["A"] + list(Code)
    string = ''.join(nums)
    input = []
    for i in range(len(nums)-1):
        input.append(LastRobot(nums[i], nums[i+1]))
    # breakpoint()
    
    # input = input[1:].split("A")
    # input = list(map(lambda x: x + "A", input))
    # input.pop(-1)
    possibilities = []
    for q in range(len(input[0])):
        for w in range(len(input[1])):
            for e in range(len(input[2])):
                for r in range(len(input[3])):
                    Pieces = Counter()
                    Cache = Counter()
                    Pieces[input[0][q]] += 1
                    Pieces[input[1][w]] += 1
                    Pieces[input[2][e]] += 1
                    Pieces[input[3][r]] += 1
                    
                    for i in range(25):
                        if i == 1 and Code == "179A":
                            breakpoint()
                            pass
                        for p in list(Pieces.keys()):
                            result = Robots(p)
                            result = result.split("A")
                            result = list(map(lambda x: x + "A", result))
                            result.pop(-1)
                            for item in result:
                                Cache[item] += Pieces[p]
                        Pieces = Counter(Cache)
                        Cache = Counter()
                    output = 0
                    for a in list(Pieces.keys()):
                        output += len(a) * Pieces[a]
                    # breakpoint()
                    possibilities.append(output)
    print(possibilities)
    print(int(string.replace("A", "")))
    return min(possibilities) * int(string.replace("A", ""))

    

with open("input21.txt", "r") as f:
    Codes = f.readlines()
    Codes = list(map(lambda x: x.replace("\n", ""), Codes))
    print(Codes)
    total = 0
    for j in Codes:
        if j == "789A":
            # breakpoint()
            pass
        total += Solve(j)
    print(total)

