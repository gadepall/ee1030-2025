import numpy as np
import matplotlib.pyplot as plt
import math

angle = int(input("Input the angle that the line subtends on the major segment."))

angle = angle*3.1415/180

rotation = np.array([[math.cos(angle), math.sin(angle)],
                    [-math.sin(angle), math.cos(angle)]])

answer2 = np.linalg.matmul( [0,1], rotation)

answer2[0] = round(answer2[0],2)
answer2[1] = round(answer2[1],2)

answer1 = np.linalg.matmul( rotation, [0,1])

answer1[0] = round(answer1[0],2)
answer1[1] = round(answer1[1],2)


def slope(x1,y1,x2,y2):
    return( ( y2-y1)/(x2-x1))

slope1 = slope(answer1[0], answer1[1], 0, 1)

slope2 = (slope(answer2[0], answer2[1], 0, 1))

print(slope1,slope2)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)

X = np.linspace(-10,10,20)

Y1 = slope1*X + 1
Y2 = slope2*X + 1

ax.plot(X,Y1, label = 'Line 1')
ax.plot(X,Y2, label ='Line 2')
ax.scatter(0,1, label='(0,1)')
ax.scatter(answer1[0], answer1[1], label='POI 1')
ax.scatter(answer2[0], answer2[1], label = 'POI 2')

circle = plt.Circle((0, 0), 1, color='grey', fill=False, linewidth=1)
ax.add_patch(circle)

ax.legend()
ax.grid(True)
plt.show()