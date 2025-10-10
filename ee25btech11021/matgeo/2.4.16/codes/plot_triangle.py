
import sys
sys.path.insert(0,  '/home/dhanush-sagar/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt

# Local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Load both sets of points
iso_points = np.loadtxt("iso_points.dat")
right_points = np.loadtxt("right_points.dat")

# ---- Plot Isosceles Triangle ----
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
A, B, C = iso_points
tri_iso = np.vstack((A, B, C, A))
ax1.plot(tri_iso[:,0], tri_iso[:,1], tri_iso[:,2], 'b-o', label='Isosceles Triangle')
ax1.text(A[0], A[1], A[2], "A", color='red')
ax1.text(B[0], B[1], B[2], "B", color='red')
ax1.text(C[0], C[1], C[2], "C", color='red')
ax1.set_title("Isosceles Triangle")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.set_zlabel("Z-axis")
plt.legend()
plt.savefig("isosceles_triangle.png")
plt.show()

# ---- Plot Right-Angled Triangle ----
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
P, Q, R = right_points
tri_right = np.vstack((P, Q, R, P))
ax2.plot(tri_right[:,0], tri_right[:,1], tri_right[:,2], 'g-o', label='Right-Angled Triangle')
ax2.text(P[0], P[1], P[2], "P", color='red')
ax2.text(Q[0], Q[1], Q[2], "Q", color='red')
ax2.text(R[0], R[1], R[2], "R", color='red')
ax2.set_title("Right-Angled Triangle")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")
ax2.set_zlabel("Z-axis")
plt.legend()
plt.savefig("right_triangle.png")
plt.show()

