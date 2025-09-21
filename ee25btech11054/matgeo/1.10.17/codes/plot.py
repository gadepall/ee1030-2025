import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./vector.so")
lib.generate_points.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double)
]

def get_points(vector, n=20):
    vec = (ctypes.c_double * 3)(*vector)
    points = np.zeros((n, 3), dtype=np.float64)
    lib.generate_points(vec, n, points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
    return points


a = np.array([2, 2, -5], dtype=np.float64)
b = np.array([2, 1, 3], dtype=np.float64)
s = a + b
unit_s = s / np.linalg.norm(s)


pa = get_points(a)
pb = get_points(b)
ps = get_points(s)
pu = get_points(unit_s)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(pa[:,0], pa[:,1], pa[:,2], label='a')
ax.plot(pb[:,0], pb[:,1], pb[:,2], label='b')
ax.plot(ps[:,0], ps[:,1], ps[:,2], label='a+b')
ax.plot(pu[:,0], pu[:,1], pu[:,2], label='unit (a+b)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.savefig("../figs/plot.png")
plt.show()

