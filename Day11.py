import regex as re #A little but of regex in your diet is healthy
from functools import cache
from collections import Counter
Zero = re.compile(r'^0+')
@cache
def SplitOrNo(Rock):
    global Zero
    if bool(re.search(Zero, Rock)):
        return "1"
    elif len(Rock) % 2 == 0:
        # breakpoint()
        Part1, Part2 = Rock[:(int((len(Rock)/2)))], Rock[(int(len(Rock)/2)):]
        return [Part1, str(int(Part2))]
    else:
        return str(int(Rock) * 2024)

def P1():
    with open("input11.txt", "r") as f:
        Stones = f.readline().split(" ")
        Rocks = Counter()
        Cache = Counter() # Ignore the clearly incorrect name
        for i in Stones:
            Rocks[i] = 1

        for i in range(75):
            Numbers = list(Rocks.keys())
            for num in Numbers:
                result = SplitOrNo(num)
                if type(result) == list:
                    Cache[result[0]] += Rocks[num]
                    Cache[result[1]] += Rocks[num]
                else:
                    Cache[result] += Rocks[num]
            # breakpoint()
            Rocks = Counter(Cache)
            Cache = Counter()
        


        print(Cache)
        print(Rocks.total())

P1()