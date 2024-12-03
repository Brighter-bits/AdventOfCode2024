import regex as re

def p1():
    with open("input3.txt", "r") as f:
        input = f.read()
        regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
        muls = re.findall(regex, input)
        print(input)
        muls = list(map(lambda x: x.strip("mul()").split(","), muls))
        totals = []
        for i in range(len(muls)):
            totals.append(int(muls[i][0])*int(muls[i][1]))
        print(sum(totals))

def p2():
    with open("input3.txt", "r") as f:
        input = f.read()
        regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")
        muls = re.findall(regex, input)
        muls = list(map(lambda x: x.strip("mul()").split(","), muls))
        dos = []
        donts = []
        count = 0
        next = 0
        while True:
            try:
                dos.append(muls.index(['do'], next+1))
                next = dos[count]
                count += 1
            except:
                break

        count = 0
        next = 0

        Tmults = []
        while True:
            try:
                donts.append(muls.index(['don\'t'], next+1))
                next = donts[count]
                count += 1
            except:
                break
        do = True
        index = 0
        print(len(muls))
        while True:
            try:
                dos = [e for e in dos if e > index]
                donts = [e for e in donts if e > index]
                if index in dos:
                    print("T")
                else:
                    print("F")
                print(index)
                if do == [] or donts == []:
                    Tmults.extend(muls[index:])
                    break
                if do:
                    Tmults.extend(muls[index:donts[0]])
                    index = donts[0]
                    do = False
                else:
                    index = dos[0]
                    do = True
            except Exception as e:
                print(e)
                break
        print(len(Tmults))
        Tmults = [e for e in Tmults if e != ["do"] and e != ["don't"]]
        print(len(Tmults))
        totals = []
        for i in range(len(Tmults)):
            totals.append(int(Tmults[i][0])*int(Tmults[i][1]))
        print(sum(totals))

p2()