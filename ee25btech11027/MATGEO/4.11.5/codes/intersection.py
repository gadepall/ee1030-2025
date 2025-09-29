import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib = ctypes.CDLL("./intersection.so")   # use "plane.dll" on Windows

# Prepare output buffer (7 doubles)
out = (ctypes.c_double * 7)()
lib.solve(out)

# Extract results
n = [out[0], out[1], out[2], out[3]]
intersection = [out[4], out[5], out[6]]

print(f"Equation of plane: {n[0]}x + {n[1]}y + {n[2]}z + {n[3]} = 0")
print(f"Intersection point: {intersection}")

# --- Plotting ---
A = np.array([2,5,-3])
B = np.array([-2,-3,5])
C = np.array([5,3,-3])
P = np.array([3,1,5])
Q = np.array([-1,-3,-1])
I = np.array(intersection)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot the plane
xx, yy = np.meshgrid(range(-2,7), range(-4,7))
zz = (-n[0]*xx - n[1]*yy - n[3]) / n[2]
ax.plot_surface(xx, yy, zz, alpha=0.3, color="cyan")

# Plot line PQ
t_vals = np.linspace(-1,2,20)
linePQ = np.array([P + t*(Q-P) for t in t_vals])
ax.plot(linePQ[:,0], linePQ[:,1], linePQ[:,2], "g", label="Line PQ")

# Plot points
ax.scatter(*A, color="r", s=50, label="A(2,5,-3)")
ax.scatter(*B, color="b", s=50, label="B(-2,-3,5)")
ax.scatter(*C, color="m", s=50, label="C(5,3,-3)")
ax.scatter(*I, color="k", s=80, marker="o", label="Intersection F(1,-1,2)")
ax.text(2, 5, -3, "A", color="red", fontsize=12)
ax.text(-2, -3, 5, "B", color="blue", fontsize=12)
ax.text(5, 3, -3, "c", color="purple", fontsize=12)
ax.text(1, -1, 2, "F", color="black", fontsize=12)


ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/4.11.5/figs/figure1.png")
plt.show()
