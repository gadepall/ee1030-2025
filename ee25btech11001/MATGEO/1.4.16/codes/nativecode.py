import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Load shared library ---
lib = ctypes.CDLL("./code.so")

# Configure ctypes function signature
lib.findM.argtypes = [ctypes.c_float, ctypes.c_float,
                      ctypes.c_float, ctypes.c_float, ctypes.c_float]
lib.findM.restype = ctypes.c_float

def point_on_line(A, B, Px):
    """Compute (x,y,z) for given Px using the C function findM"""
    Ax, Ay, Az = A
    Bx, By, Bz = B
    y = lib.findM(Ax, Ay, Bx, By, Px)
    z = lib.findM(Ax, Az, Bx, Bz, Px)
    return np.array([Px, y, z], dtype=float)

# --- Given points ---
P = np.array([4.0,  2.0, -6.0])
Q = np.array([10.0, -16.0, 6.0])

# Trisection (1:2 and 2:1 ratios)
Rx = (2*P[0] + Q[0]) / 3
Sx = (P[0] + 2*Q[0]) / 3

R = point_on_line(P, Q, Rx)
S = point_on_line(P, Q, Sx)


# --- Plotting ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Line PQ
ax.plot([P[0],Q[0]], [P[1],Q[1]], [P[2],Q[2]], label='$PQ$', color="blue")

# Collect points
points = np.stack([P,Q,R,S], axis=1)
ax.scatter(points[0,:], points[1,:], points[2,:], color="red", s=50)

# Labels with offsets + dotted connectors (like your provided code)
labels = ['P','Q','R','S']
offsets = [(5,5,5), (5,-5,5), (-5,5,5), (5,5,-5)]  # tweak to avoid overlap

for i, txt in enumerate(labels):
    dx, dy, dz = offsets[i]
    ax.text(points[0,i]+dx, points[1,i]+dy, points[2,i]+dz,
            f'{txt}({points[0,i]:.0f},{points[1,i]:.0f},{points[2,i]:.0f})',
            fontsize=9, color="black")
    ax.plot([points[0,i], points[0,i]+dx],
            [points[1,i], points[1,i]+dy],
            [points[2,i], points[2,i]+dz],
            color="gray", linestyle="dotted")

# Equal axis scaling
max_range = np.array([points[0,:].max()-points[0,:].min(),
                      points[1,:].max()-points[1,:].min(),
                      points[2,:].max()-points[2,:].min()]).max() / 2.0

mid_x = (points[0,:].max()+points[0,:].min()) * 0.5
mid_y = (points[1,:].max()+points[1,:].min()) * 0.5
mid_z = (points[2,:].max()+points[2,:].min()) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Beautify
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend()
ax.grid(True)

plt.show()

