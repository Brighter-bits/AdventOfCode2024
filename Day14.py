from collections import Counter
import numpy as np
import matplotlib.pyplot as Mat
from PIL import Image as I
def P1():
    with open("input14.txt", "r") as f:
        input = f.readlines()
        Robots = []
        for i in range(len(input)):
            Parts = input[i].replace('v=', "").replace("p=", "").replace("\n", "").split(" ")
            for j in range(len(Parts)):
                Parts[j] = list(map(int, Parts[j].split(",")))
            Pieces = []
            Parts[1][0] *= 100
            Parts[1][1] *= 100

            XCoord = Parts[0][0] + Parts[1][0]
            YCoord = Parts[0][1] + Parts[1][1]
            Pieces.append([XCoord%101, YCoord%103])
            Robots.append(Pieces)
            print(XCoord%101)
        print(Robots)

        TL = [e for e in Robots if e[0][0] < 50 and e[0][1] < 51]
        TR = [e for e in Robots if e[0][0] > 50 and e[0][1] < 51]
        BL = [e for e in Robots if e[0][0] < 50 and e[0][1] > 51]
        BR = [e for e in Robots if e[0][0] > 50 and e[0][1] > 51]
        # print(TL)
        # print(TR)
        # print(BL)
        # print(BR)
        print(len(TL) * len(TR) * len(BR) * len(BL))
        # [[XCoord, YCoord] , [XVelo, Y Velo]]

def P2():
    with open("input14.txt", "r") as f:
        input = f.readlines()
        Robots = []
        for i in range(len(input)):
            Parts = input[i].replace('v=', "").replace("p=", "").replace("\n", "").split(" ")
            for j in range(len(Parts)):
                Parts[j] = list(map(int, Parts[j].split(",")))
            # [[XCoord, YCoord] , [XVelo, Y Velo]]
            Robots.append(Parts)
        count = 18
        while True:
            RoboIter = []
            for i in range(len(Robots)):
                RoboIter.append([(Robots[i][0][0] + (Robots[i][1][0] * count))%101, (Robots[i][0][1] + (Robots[i][1][1] * count))%103])
            # # Why look for the christmas tree when you can look for the border?
            # XCoords = Counter()
            # YCoords = Counter()
            # for i in range(len(RoboIter)):    ######## Why do Fancy stuff when you can brute force
            #     XCoords[RoboIter[i][0]] += 1
            #     YCoords[RoboIter[i][1]] += 1
            # # Find the two most common of each coord which is probably the border, then check if the corners are filled in or not
            # CommonX = XCoords.most_common(2)
            # CommonY = YCoords.most_common(2)
            Image = [["0" for a in range(101)] for b in range(103)]
            # if [CommonX[0][0], CommonY[0][0]] in RoboIter and [CommonX[1][0], CommonY[0][0]] in RoboIter and [CommonX[0][0], CommonY[1][0]] in RoboIter and [CommonX[1][0], CommonY[1][0]] in RoboIter:
            for i in range(len(RoboIter)):
                Image[RoboIter[i][1]][RoboIter[i][0]] = "255"
            Image = np.array(Image)
            # print(type(Image))
            I.fromarray(Image.astype(np.uint8)).save(("D14/" + str(count) + ".jpg"))
            # Mat.imsave(("/D14/" + str(count) + ".png"), Image)
            count += 101
            # break
            if count == 10118:
                break
P2()