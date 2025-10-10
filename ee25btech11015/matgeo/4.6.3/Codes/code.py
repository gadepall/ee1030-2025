import numpy as np
import matplotlib.pyplot as plt
import ctypes

# --- Load the compiled C library ---
c_lib = ctypes.CDLL('./line.so')

# Define argument & return types
c_lib.line_point.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                             ctypes.c_float, ctypes.c_float, ctypes.c_float,
                             ctypes.c_float,
                             ctypes.POINTER(ctypes.c_float)]

# --- Given point & direction vector ---
P = (-2.0, 4.0, -5.0)   # point
d = (3.0, 5.0, 6.0)     # direction vector

# --- Generate points on the line using C function ---
t_values = np.linspace(-5, 5, 50)
line_points = []

for t in t_values:
    coords = (ctypes.c_float * 3)()  # array of 3 floats
    c_lib.line_point(P[0], P[1], P[2],
                     d[0], d[1], d[2],
                     ctypes.c_float(t), coords)
    line_points.append([coords[0], coords[1], coords[2]])

line_points = np.array(line_points)

# --- Plot the line ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], 
        color="red", label="Required Line")
ax.scatter(P[0], P[1], P[2], color="green", s=50)
ax.text(P[0], P[1], P[2], "P(-2,4,-5)", color="green")

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Line through P(-2,4,-5) with direction (3,5,6)")
ax.legend()
plt.show()
