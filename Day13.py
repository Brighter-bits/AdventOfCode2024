from decimal import Decimal
with open("input13.txt", "r") as f:
    input = f.read()
    input =  list(map(lambda x: x.split("\n"), input.split("\n\n")))
    Cranes = []
    total = 0
    for i in range(len(input)):
        ButA = list(map(int, input[i][0].replace("Button A: ", "").replace("X+", "").replace("Y+", "").replace(" ", "").split(",")))
        ButB = list(map(int, input[i][1].replace("Button B: ", "").replace("X+", "").replace("Y+", "").replace(" ", "").split(",")))
        Target = list(map(int, input[i][2].replace("Prize: ", "").replace("X=", "").replace("Y=", "").replace(" ", "").split(",")))
        Target[0] += 10000000000000
        Target[1] += 10000000000000
        Cranes.append([ButA, ButB, Target])
    for i in range(len(Cranes)):
        # XFactor = math.gcd(Cranes[i][0][0], Cranes[i][1][0])
        # YFactor = math.gcd(Cranes[i][0][1], Cranes[i][1][1])
        # if Cranes[i][2][0] % XFactor == 0:
        #     Cranes[i][0][0] = int(Cranes[i][0][0]/XFactor)
        #     Cranes[i][1][0] = int(Cranes[i][1][0]/XFactor)
        #     Cranes[i][2][0] = int(Cranes[i][2][0]/XFactor)
        # if Cranes[i][2][1] % YFactor == 0:
        #     Cranes[i][0][1] = int(Cranes[i][0][1]/YFactor)
        #     Cranes[i][1][1] = int(Cranes[i][1][1]/YFactor)
        #     Cranes[i][2][1] = int(Cranes[i][2][1]/YFactor)
        # Continue = True
        # if i == 2:
        # breakpoint()
        MultA = Decimal(Cranes[i][1][1]/Cranes[i][1][0]) # Made from Y
        Step1 = ((Decimal(Cranes[i][2][0]))*MultA) # Taking this out makes it work, IDK why
        a = round(float((Step1-Decimal(Cranes[i][2][1]))/((Decimal((Cranes[i][0][0]))*MultA)-(Decimal(Cranes[i][0][1])))), 3)
        if a.is_integer():
            b = round(float((Cranes[i][2][0]-(a*Cranes[i][0][0]))/Cranes[i][1][0]), 6)
            if b.is_integer():
                print(a, b, i+1)
                total += (int(a)*3) + int(b)
        
    print(total)