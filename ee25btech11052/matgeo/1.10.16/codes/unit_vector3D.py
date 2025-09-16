import ctypes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lib = ctypes.CDLL('/home/shriyasnh/Desktop/matgeo/1.10.16/codes/libunit3d.so')
lib.unit_vector3d.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

x, y, z = ctypes.c_double(2.0), ctypes.c_double(3.0), ctypes.c_double(6.0)

lib.unit_vector3d(ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
u = (x.value, y.value, z.value)
print("Unit vector:", u)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

axis_len = 1.5
ax.quiver(0,0,0, axis_len,0,0, color="k", arrow_length_ratio=0.05)
ax.quiver(0,0,0, 0,axis_len,0, color="k", arrow_length_ratio=0.05)
ax.quiver(0,0,0, 0,0,axis_len, color="k", arrow_length_ratio=0.05)

ax.text(axis_len+0.05, 0, 0, "X", fontsize=12)
ax.text(0, axis_len+0.05, 0, "Y", fontsize=12)
ax.text(0, 0, axis_len+0.05, "Z", fontsize=12)

ax.quiver(0, 0, 0, u[0], u[1], u[2], color='r', arrow_length_ratio=0.1)

coord_label = f"({u[0]:.2f}, {u[1]:.2f}, {u[2]:.2f})"
ax.text(u[0]+0.1, u[1]+0.1, u[2]+0.1, coord_label, fontsize=10, color='r')

ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Unit Vector from C Function")


plt.show()