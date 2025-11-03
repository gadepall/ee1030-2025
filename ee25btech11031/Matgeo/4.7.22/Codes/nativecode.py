import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

a = 31
b = 63
c = 31
P = np.array([1,2])

roots = np.roots([a,b,c])

t = (2+roots[0])/(roots[0]+1)

A = np.array([t,4-t], dtype = np.double)

k = (2+roots[1])/(roots[1]+1)

B = np.array([k, 4-k], dtype = np.double)

plt.plot([-5,8], [9,-4], label = "$x+y=4$")
plt.plot([P[0],A[0]], [P[1], A[1]])
plt.plot([P[0],B[0]], [P[1], B[1]])

plt.scatter([1,t,k],[2,4-t,4-k])
plt.annotate(
        "P(1,2)",
        xy=(1,2),
        xytext = (-15,-15),
        textcoords = "offset points"
        )

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig("../Figs/plot(py).png")
plt.show()

