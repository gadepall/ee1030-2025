import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import math

matrix = np.array([[math.cos(math.pi/4), math.cos(5*math.pi/6)],
                   [math.sin(math.pi/4), math.sin(5*math.pi/6)]])

vec = np.array([0,100])

norms = np.linalg.solve(matrix,vec)

print(norms)

fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111)

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax.quiver(0,0,0,-100, color = 'Blue', label = 'P = 100N',  angles='xy', scale_units='xy', scale=1)
ax.quiver(0,0, norms[0]*matrix[0,0], norms[0]*matrix[1,0], color = 'green', label = f"$T_1 = ${round(norms[0],2)}N",  angles='xy', scale_units='xy', scale=1)
ax.quiver(0,0, norms[1]*matrix[0,1], norms[0]*matrix[1,1], color = 'orange', label = f"$T_2 = ${round(norms[1],2)}N",  angles='xy', scale_units='xy', scale=1)


ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.legend()
ax.grid(True)
plt.show()