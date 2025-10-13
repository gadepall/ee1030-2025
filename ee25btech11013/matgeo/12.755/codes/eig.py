import numpy as np
import ctypes
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

lib = ctypes.CDLL("./libplanes.so")

N = 40
d = np.linspace(-2, 2, N)
Y, Z = np.meshgrid(d, d)
X = np.zeros_like(Y)

# Convert to C-contiguous arrays
Y_c = np.ascontiguousarray(Y, dtype=np.double)
Z_c = np.ascontiguousarray(Z, dtype=np.double)
X_c = np.ascontiguousarray(X, dtype=np.double)

# Set argument types
lib.generate_plane1.argtypes = [np.ctypeslib.ndpointer(dtype=np.double),
                                np.ctypeslib.ndpointer(dtype=np.double),
                                np.ctypeslib.ndpointer(dtype=np.double),
                                ctypes.c_int]

lib.generate_plane2.argtypes = [np.ctypeslib.ndpointer(dtype=np.double),
                                np.ctypeslib.ndpointer(dtype=np.double),
                                np.ctypeslib.ndpointer(dtype=np.double),
                                ctypes.c_int]

lib.generate_intersection_line.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                           np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                           np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                           ctypes.c_int]

# Generate plane1
lib.generate_plane1(Y_c, Z_c, X_c, N)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X_c, Y_c, Z_c, alpha=0.5, color='g')

# Plane 2
X2, Z2 = np.meshgrid(d, d)
Y2 = np.zeros_like(X2)
lib.generate_plane2(X2, Z2, Y2, N)
ax.plot_surface(X2, Y2, Z2, alpha=0.5, color='r')

# Intersection line
x_line = np.zeros(N)
y_line = np.zeros(N)
z_line = np.zeros(N)
lib.generate_intersection_line(x_line, y_line, z_line, N)
ax.plot3D(x_line, y_line, z_line, color='k', linewidth=3)

# Intersection point at origin
ax.scatter(0,0,0,color='black',s=80)

# Legend
legend_elements = [
    Line2D([0],[0], color='g', lw=4, alpha=0.5, label='x - 2y = 0'),
    Line2D([0],[0], color='r', lw=4, alpha=0.5, label='y = 0'),
    Line2D([0],[0], color='k', lw=3, label='Intersection Line (x=0, y=0)'),
    Line2D([0],[0], marker='o', color='k', label='Origin (0,0,0)', markersize=8, linestyle='')
]
ax.legend(handles=legend_elements)

ax.set_xlabel('X-axis'); ax.set_ylabel('Y-axis'); ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Planes: x - 2y = 0 and y = 0')
ax.view_init(elev=25, azim=-60)

plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.755/figs/Figure_1.png")

plt.show()
