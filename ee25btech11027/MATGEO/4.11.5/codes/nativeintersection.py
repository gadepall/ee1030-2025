import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---- Step 1: Define points ----
A = np.array([2, 5, -3])
B = np.array([-2, -3, 5])
C = np.array([5, 3, -3])
P = np.array([3, 1, 5])
Q = np.array([-1, -3, -1])
I = np.array(intersection)

# ---- Step 2: Find plane equation ----
AB = B - A
AC = C - A
n = np.cross(AB, AC)          # normal vector
d = -np.dot(n, A)             # plane constant

print(f"Equation of plane: {n[0]}x + {n[1]}y + {n[2]}z + {d} = 0")

# ---- Step 3: Find intersection of plane with line PQ ----
v = Q - P
t = -(np.dot(n, P) + d) / np.dot(n, v)
intersection = P + t*v

print("Intersection point:", intersection)

# ---- Step 4: Plot everything ----
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plane surface
xx, yy = np.meshgrid(range(-2, 7), range(-4, 7))
zz = (-n[0]*xx - n[1]*yy - d) / n[2]
ax.plot_surface(xx, yy, zz, alpha=0.3, color="cyan")

# Line PQ
t_vals = np.linspace(-1, 2, 20)
linePQ = np.array([P + t*(Q-P) for t in t_vals])
ax.plot(linePQ[:,0], linePQ[:,1], linePQ[:,2], 'g', label="Line PQ")

# Highlight points
ax.scatter(*A, color='r', s=50, label="A(2,5,-3)")
ax.scatter(*B, color='b', s=50, label="B(-2,-3,5)")
ax.scatter(*C, color='m', s=50, label="C(5,3,-3)")
ax.scatter(*I, color="k", s=80, marker="o", label="Intersection F(1,-1,2)")
ax.text(2, 5, -3, "A", color="red", fontsize=12)
ax.text(-2, -3, 5, "B", color="blue", fontsize=12)
ax.text(5, 3, -3, "c", color="purple", fontsize=12)
ax.text(1, -1, 2, "F", color="black", fontsize=12)

# Connecting AB (dashed line like your figure)
ax.plot([A[0],B[0]], [A[1],B[1]], [A[2],B[2]], '--', color="black", label="Connecting AB")

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/4.11.5/figs/figure1.png")
plt.show()
