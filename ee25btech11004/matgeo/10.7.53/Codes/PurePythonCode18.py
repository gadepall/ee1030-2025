import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg
import math

X = np.linspace(-10,10,100)
Y = np.linspace(-10,10,100)

Y1 = X*X+1
X1 = Y*Y+1

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(111)

ax.plot(X,Y1)
ax.plot(X1,Y)
ax.scatter(1,2, label= 'P')
ax.scatter(2,1, label = '$P_i$')
ax.scatter(5,2, label = 'Q')
ax.scatter(2,5, label = '$Q_i$')

# Data for the line segments
x1, y1 = [1, 2], [2, 1]
x2, y2 = [2, 5], [5, 2]
x3, y3 = [1, 5], [2, 2]

# Plotting the line segments
plt.plot(x1, y1, marker='o')
plt.plot(x2, y2, marker='o')
plt.plot(x3, y3, marker='o', color = 'black')


ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')





ax.legend()
ax.grid(True)
plt.show()