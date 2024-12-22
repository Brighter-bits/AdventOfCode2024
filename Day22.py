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

def P1(nums):
    for i in range(len(nums)):
        Number = nums[i]
        for j in range(2000):
            Number = SecretMaker(Number)
        nums[i] = Number
    print(sum(nums))


def DifferenceMaker(nums):
    Differences = []
    Prices = []
    for i in range(len(nums)):
        Price = [nums[i]]
        Distances = ['#']
        OldNumber = nums[i]
        for j in range(2000):
            NewNumber = SecretMaker(OldNumber)
            # Distance = int(str(NewNumber)[-1]) - int(str(OldNumber)[-1])
            Distance = str((NewNumber%10) - (OldNumber%10)) # Mod 10 is a lot faster
            Distances.append(Distance)
            OldNumber = NewNumber
            Price.append(OldNumber%10)
        Distances = ','.join(Distances)
        Differences.append(Distances)
        Prices.append(Price)
    return Differences, Prices

def P2(nums):
    Differences, Prices = DifferenceMaker(nums)
    PossiblePrices = []
    for z in range(-9, 10):
        for x in range(-9, 10):
            for c in range(-9, 10):
                for v in range(-9, 10):
                    sequence = "," + str(z) + "," + str(x) + "," + str(c) + "," + str(v)
                    # if sequence == "1,2,-6,6":
                    #     breakpoint()
                    print(sequence)
                    total = 0
                    for monkey in range(len(Differences)):
                        if sequence in Differences[monkey]:
                            Index = Differences[monkey].count(",", 0, (Differences[monkey].index(sequence)+len(sequence)))
                            total += Prices[monkey][Index]
                    # if total == 27:
                    #     Bob = sequence
                    PossiblePrices.append(total)
    # breakpoint()
    print(max(PossiblePrices))



    

with open("input22.txt", "r") as f:
    Numbers = f.readlines()
    Numbers = list(map(lambda x: int(x.replace("\n", "")), Numbers))
    # P1(Numbers)
    P2(Numbers)
