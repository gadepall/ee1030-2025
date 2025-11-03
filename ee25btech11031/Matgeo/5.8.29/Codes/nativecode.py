import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

M = np.array([[2,5],
              [3,6]])
b = np.array([1/4,1/3])
x = LA.solve(M, b)


plt.scatter(x[0],x[1])

x[0]=np.round(x[0],3)
x[1]=np.round(x[1],3)

plt.plot([-2,2], [0.85,-0.75], c='red', label = r"$2x+5y=\frac{1}{4}$")
plt.plot([-2,2], [19/18,-17/18], c='black', label = r"$3x+6y=\frac{1}{3}$")

plt.annotate(
        f"{x[0],x[1]}",
        xy=(x[0],x[1]),
        xytext = (2,2),
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


