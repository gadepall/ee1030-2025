import ctypes
import numpy as np
import matplotlib.pyplot as plt

c_lib = ctypes.CDLL("./code.so")

c_lib.Gaussian.argtypes = [ctypes.c_double*3, ctypes.c_double*3, ctypes.c_double*2]


A = (ctypes.c_double*3)(1,1,5)
B = (ctypes.c_double*3)(2,-3,4)

sols = (ctypes.c_double*2)(0.0,0.0)

c_lib.Gaussian(A,B,sols)

plt.plot([-1,5.5], [6,-0.5], c='green', label = "$x+y=5$")
plt.plot([-1,5], [-2,2], c='blue', label = "$2x-3y=4$")

plt.scatter(sols[0],sols[1])

plt.annotate(
        f"{sols[0],sols[1]}",
        xy=(sols[0],sols[1]),
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

plt.savefig("../Figs/plot(py+C).png")
plt.show()


