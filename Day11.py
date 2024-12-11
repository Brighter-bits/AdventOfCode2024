import regex as re #A little but of regex in your diet is healthy
def P1():
    with open("input11.txt", "r") as f:
        Stones = f.readline().split(" ")
        Zero = re.compile(r'^0+')
        for i in range(75):
            # breakpoint()
            Cache = []
            for number in range(len(Stones)):
                # breakpoint()
                if bool(re.search(Zero, Stones[number])):
                    Cache.append("1")
                elif len(Stones[number]) % 2 == 0:
                    # breakpoint()
                    Part1, Part2 = Stones[number][:(int((len(Stones[number])/2)))], Stones[number][(int(len(Stones[number])/2)):]
                    Cache.append(str(int(Part1)))
                    Cache.append(str(int(Part2)))
                else:
                    Cache.append(str(int(Stones[number]) * 2024)) 
            Stones = list(Cache)
            print(i, len(Stones))
        print(len(Stones))

P1()