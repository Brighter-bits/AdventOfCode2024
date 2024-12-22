from functools import cache
import math
Mix = cache((lambda x, y: x^y))

Prune = cache((lambda x: x%16777216))

MixPrune = cache((lambda x, y: Prune(Mix(x, y))))

@cache
def SecretMaker(num):
    num = MixPrune(num, (num*64))
    num = MixPrune(num, math.floor(num/32))
    num = MixPrune(num, (num*2048))
    return num

with open("input22.txt", "r") as f:
    Numbers = f.readlines()
    Numbers = list(map(lambda x: int(x.replace("\n", "")), Numbers))
    for i in range(len(Numbers)):
        Number = Numbers[i]
        for j in range(2000):
            Number = SecretMaker(Number)
        Numbers[i] = Number
    print(sum(Numbers))
