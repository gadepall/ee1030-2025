import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

so = ctypes.CDLL("./find_parallelepiped_vol.so")


# Function signature
# double parallelepiped_volume(double *a, double *b, double *c)
so.parallelepiped_volume.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
so.parallelepiped_volume.restype = ctypes.c_double

# Define vectors
a = np.array([1, 0, 0], dtype=np.double)
b = np.array([0.5, np.sqrt(3)/2, 0], dtype=np.double)
c = np.array([0.5, 1/(2*np.sqrt(3)), np.sqrt(2/3)], dtype=np.double)

# Pointers for ctypes
a_ptr = a.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
b_ptr = b.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
c_ptr = c.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call C function
volume = so.parallelepiped_volume(a_ptr, b_ptr, c_ptr)

# Vertices of parallelepiped
p1 = np.array([0,0,0])
p2 = a
p3 = b
p4 = c
p5 = a+b
p6 = b+c
p7 = c+a
p8 = a+b+c

# Plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# Bottom face
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'grey')
ax.plot([p1[0], p3[0]], [p1[1], p3[1]], [p1[2], p3[2]], 'grey')
ax.plot([p2[0], p5[0]], [p2[1], p5[1]], [p2[2], p5[2]], 'grey')
ax.plot([p3[0], p5[0]], [p3[1], p5[1]], [p3[2], p5[2]], 'grey')

# Top face
ax.plot([p4[0], p7[0]], [p4[1], p7[1]], [p4[2], p7[2]], 'grey')
ax.plot([p4[0], p6[0]], [p4[1], p6[1]], [p4[2], p6[2]], 'grey')
ax.plot([p7[0], p8[0]], [p7[1], p8[1]], [p7[2], p8[2]], 'grey')
ax.plot([p6[0], p8[0]], [p6[1], p8[1]], [p6[2], p8[2]], 'grey')

# Vertical edges
ax.plot([p1[0], p4[0]], [p1[1], p4[1]], [p1[2], p4[2]], 'grey')
ax.plot([p2[0], p7[0]], [p2[1], p7[1]], [p2[2], p7[2]], 'grey')
ax.plot([p3[0], p6[0]], [p3[1], p6[1]], [p3[2], p6[2]], 'grey')
ax.plot([p5[0], p8[0]], [p5[1], p8[1]], [p5[2], p8[2]], 'grey')

# Legend with computed volume
ax.plot([], [], [], 'grey', label=f"Parallelepiped of volume {volume:.4f}")

# Labels
ax.set_xlabel("X - AXIS")
ax.set_ylabel("Y - AXIS")
ax.set_zlabel("Z - AXIS")
ax.set_title("Parallelepiped with a·b = b·c = c·a = 1/2")
ax.legend()
ax.set_box_aspect([1,1,1])
ax.view_init(elev=15, azim=135)

plt.savefig("parallelepiped_volume.png", dpi=300)
plt.show()
