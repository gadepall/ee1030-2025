import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA


M = np.array([[1, 1],
              [2,-3]])
b = np.array([5,4])
x = LA.solve(M, b)


plt.scatter(x[0],x[1])

plt.plot([-1,5.5], [6,-0.5], c='red', label = '$x+y=5$')
plt.plot([-1,5], [-2,2], c='blue', label = '$2x-3y=4$')

plt.annotate(
        f'{x[0],x[1]}',
        xy=(x[0],x[1]),
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


