Numbers = []
FirstNums = []
SecondNums = []
with open("input1.txt", "r") as f:
    Numbers = f.readlines()
    Numbers = list(map(lambda x: x.replace("\n", "").split("   "), Numbers))
    FirstNums = sorted(map(int, list(map(lambda x: x[0], Numbers))))
    SecondNums = sorted(map(int, list(map(lambda x: x[1], Numbers))))
    print(f"Answer1: {sum(list(map(lambda x, y: abs(x-y), FirstNums, SecondNums)))}")
    SimilarityList = []
    for i in FirstNums:
        Occurences = SecondNums.count(i)
        SimilarityList.append(i*Occurences)
    print(f"Answer2: {sum(SimilarityList)}")
