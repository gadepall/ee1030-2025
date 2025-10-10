import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg
import math


answer = numpy.linalg.solve([[2,-3],[3,4]], [[-5,0])
distance = abs((numpy.linalg.matmul([5,-2], answer))/math.sqrt(29))

print(distance)

fig = plt.figure(figsize = (8,6))
ax = fig.add_subplot(111)

X = np.linspace(-20,20,2)
Y1 = (2*X + 5)/3
Y2 = -3*X/4
Y3= 5*X/2



ax.plot(X,Y1, label='2x-3y+5=0')
ax.plot(X,Y2, label='3x+4y=0')
ax.plot(X,Y3, label ='5x-2y=0')


ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("Plot of the Three Lines")

ax.scatter(answer[0], answer[1], label=f'point of intersection({answer[0]},{answer[1]})', color='red')


ax.legend()
ax.grid(True)
plt.show()


