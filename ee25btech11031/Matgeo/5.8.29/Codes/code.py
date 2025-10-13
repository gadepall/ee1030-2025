import ctypes
import numpy as np
import matplotlib.pyplot as plt

c_lib = ctypes.CDLL("./code.so")

c_lib.Gaussian.argtypes = [ctypes.c_double*3, ctypes.c_double*3, ctypes.c_double*2]

A = (ctypes.c_double*3)(2,5,1.0/4.0)
B = (ctypes.c_double*3)(3,6,1.0/3.0)

sols = (ctypes.c_double*2)(0.0,0.0)

c_lib.Gaussian(A,B,sols)

sols[0] = np.round(sols[0],3)
sols[1] = np.round(sols[1],3)

plt.plot([-2,2], [0.85,-0.75], c='green', label = r"$2x+5y=\frac{1}{4}$")
plt.plot([-2,2], [19/18,-17/18], c='blue', label = r"$3x+6y=\frac{1}{3}$")

plt.scatter(sols[0],sols[1])

plt.annotate(
        f"{sols[0],sols[1]}",
        xy=(sols[0],sols[1]),
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

plt.savefig("../Figs/plot(py+C).png")
plt.show()


