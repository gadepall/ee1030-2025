import numpy as np
import ctypes
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./c7.so")

lib.line_point.argtypes = [
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

h = np.array([5.0, -2.0, 4.0], dtype=np.float64)
m = np.array([2.0, 1.0, 3.0], dtype=np.float64)
lambd_vals = np.linspace(-2, 2, 100)
points = np.zeros((len(lambd_vals), 3), dtype=np.float64)

for i, lam in enumerate(lambd_vals):
    lib.line_point(
        ctypes.c_double(lam),
        h.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        m.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        points[i].ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    )

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(points[:, 0], points[:, 1], points[:, 2], color='blue')
ax.scatter(h[0], h[1], h[2], color='red', s=50)
ax.text(h[0], h[1], h[2], '(5,-2,4)', color='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line from C shared library: through (5,-2,4) parallel to [2,1,3]')
plt.show()

