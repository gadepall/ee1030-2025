import ctypes
import numpy as np
import matplotlib.pyplot as plt


c_lib = ctypes.CDLL("./code.so")

c_lib.solve_quad.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double*2]

a,b,c = 31.0, 63.0, 31.0
P = np.array([1,2])
sol = (ctypes.c_double*2)(0.0,0.0)

c_lib.solve_quad(a,b,c,sol)


m1 = sol[0]
m2 = sol[1]

t = (2+m1)/(m1+1)
k = (2+m2)/(m2+1)

A = np.array([t,4-t], dtype = np.double)
B = np.array([k, 4-k], dtype = np.double)

plt.plot([-5,8], [9,-4], c='black', label = "$x+y=4$")
plt.plot([P[0],A[0]], [P[1], A[1]], c='green')
plt.plot([P[0],B[0]], [P[1], B[1]], c='red')

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

plt.savefig("../Figs/plot(py+C).png")
plt.show()


