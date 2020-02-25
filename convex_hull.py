#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.axis([-1, 20, -1, 20])
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getpoint(self):
        return self.x

    def getpointy(self):
        return self.y


def crossproduct(a, b, c):
    y1 = a.y - b.y
    y2 = a.y - c.y
    x1 = a.x - b.x
    x2 = a.x - c.x
    return y2 * x1 - y1 * x2


def distance(a, b, c):
    y1 = a.y - b.y
    y2 = a.y - c.y
    x1 = a.x - b.x
    x2 = a.x - c.x

    Y1 = y1 * y1
    X1 = x1 * x1
    Y2 = y2 * y2
    X2 = x2 * x2

    if Y1 + X1 > Y2 + X2:
        return 1
    elif Y1 + X1 < Y2 + X2:
        return -1
    else:
        return 0


listHullx = []
listHully = []

nextlistx = []
nextlisty = []



# currentlist = []

def findConvexHull(points):
    flag = 1
    start = points[0]

    for poi in points:
        if poi.x < start.x:
            start = poi

    current = start
    my_set = [start]

    collinearPoint = []

    while flag == 1:
        nextTarget = points[0]

        for point in points:
            if point == current:
                continue
            value = crossproduct(current, nextTarget, point)

            if value > 0:
                nextTarget = point
                nextlistx.append(current.getpoint())
                nextlisty.append(current.getpointy())
                nextlistx.append(nextTarget.getpoint())
                nextlisty.append(nextTarget.getpointy())
                plt.plot(nextlistx,nextlisty,'--')
                plt.pause(0.20)
                nextlistx.clear()
                nextlisty.clear()
                #nextlistx.append(nextTarget.getpoint())
                #nextlisty.append(nextTarget.getpointy())

                # currentlist.append(current)

               # print ('x_nextTarget do: ', nextTarget.getpoint(),
                       #' y_nextTarget: do ', nextTarget.getpointy())
                #print ('x_current: ', current.getpoint(), 'y_current: '
                      # , current.getpointy())
                collinearPoint.clear()
            elif value == 0:

                if distance(current, nextTarget, point) < 0:
                    collinearPoint.append(nextTarget)
                    nextTarget = point
                else:
                    collinearPoint.append(point)

        for colp in collinearPoint:
            my_set.append(colp)

        if nextTarget == start:
            #for pt in my_set:
                #listHullx.append(pt.getpoint())
                #listHully.append(pt.getpointy())
                #print ('x: ', pt.getpoint(), ' y: ', pt.getpointy())
                #print('x:: ',nextTarget.getpoint(), 'y:: ',nextTarget.getpointy())

            #listHullx.append(my_set[0].getpoint())
            #listHully.append(my_set[0].getpointy())
            #plt.plot(listHullx, listHully, '-r')
		
            flag = 0
        
        my_set.append(nextTarget)
        nextlistx.append(current.getpoint())
        nextlisty.append(current.getpointy())
        nextlistx.append(nextTarget.getpoint())
        nextlisty.append(nextTarget.getpointy())
        plt.plot(nextlistx,nextlisty,'-ko')
        nextlistx.clear()
        nextlisty.clear()
        if flag == 0:
        	nextlistx.append(current.getpoint())
        	nextlisty.append(current.getpointy())
        	nextlistx.append(start.getpoint())
        	nextlisty.append(start.getpointy())
        	print("x_current: ", current.getpoint(), "y_current: ", current.getpointy()
        		, "x_start: ",start.getpoint(), "y_start: ",start.getpointy())
        	plt.plot(nextlistx,nextlisty,'-ko')
        	plt.pause(0.20)
        current = nextTarget


p = []

N = 40
x = np.random.randint(20,size = N)
y = np.random.randint(20, size = N)

#x = [1,2,4,5,5,3,7,2,1,]
#y = [1,1,4,4,5,8,9,0,2,]

for (i, j) in zip(x, y):
    p.append(Point(i, j))
plt.plot(x, y, marker='.', linestyle='None')    
findConvexHull(p)

# print(x)
# plt.scatter(x, y)


#plt.plot(listHullx, listHully, 'r')
plt.show()

# p.append(Point(-1,1))
# p.append(Point(3,3))
# p.append(Point(2,9))
# p.append(Point(11,6))
# p.append(Point(4,2))
# p.append(Point(3,5))
# p.append(Point(4,5))

# print(p[2].getpoint())

# findConvexHull(p[0])

# p1.getpoint()
