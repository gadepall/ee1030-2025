import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lib = ctypes.CDLL("./code.so")

lib.find_line_points.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # h
    ctypes.POINTER(ctypes.c_double),  # m
    ctypes.c_double,                  # k1
    ctypes.c_double,                  # k2
    ctypes.POINTER(ctypes.c_double),  # P1
    ctypes.POINTER(ctypes.c_double)   # P2
]
lib.find_line_points.restype = None

# Input line parameters
h = np.array([5.0, -4.0, 6.0], dtype=np.float64)
m = np.array([3.0, 7.0, 2.0], dtype=np.float64)

# Prepare arrays to receive points
P1 = np.zeros(3, dtype=np.float64)
P2 = np.zeros(3, dtype=np.float64)

# Call the function
k1, k2 = -2.0, 2.0
lib.find_line_points(h.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                     m.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                     k1, k2,
                     P1.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                     P2.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

# Generate line points between P1 and P2 for plotting
line_points = np.linspace(P1, P2, 100)

# Create 3D figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# Plot the line
ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], color='blue', label=r"$\vec{x} = \vec{h} + \kappa \vec{m}$")

# Mark the given point h
ax.scatter(h[0], h[1], h[2], color='red', s=60, label=r"Point $\vec{h}(5, -4, 6)$")

# Draw the direction vector m starting at h
ax.quiver(h[0], h[1], h[2], m[0], m[1], m[2],
          color='green', arrow_length_ratio=0.1, linewidth=2, label=r"Direction $\vec{m}(3,7,2)$")

# Set axis labels and title
ax.set_xlabel("X - AXIS")
ax.set_ylabel("Y - AXIS")
ax.set_zlabel("Z - AXIS")
ax.set_title("Line: (x−5)/3 = (y+4)/7 = (z−6)/2")

# Legend and appearance
ax.legend()
ax.set_box_aspect([1,1,1])  # Equal aspect ratio
ax.view_init(elev=20, azim=130)

# Save and show
plt.savefig("fig_so.png", dpi=300)
plt.show()
