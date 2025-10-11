import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
a = np.array([2, -1, -2])      # point on line
b = np.array([3, 4, 2])        # direction vector of line
n = np.array([1, -1, 1])       # normal vector of plane
P = np.array([-1, -5, -10])    # external point

# Intersection point with plane
lam = (5 - np.dot(n, a)) / np.dot(n, b)
Q = a + lam * b

# Distance
dist = np.linalg.norm(Q - P)
print("Intersection Point Q =", Q)
print("Distance =", dist)

# Create plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot line with legend
lambdas = np.linspace(-2, 5, 100)
line_points = np.array([a + t*b for t in lambdas])
ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], 'g', label=r"$\vec{r}=2\vec{i}-\vec{j}-2\vec{k}+\lambda(3\vec{i}+4\vec{j}+2\vec{k})$")

# Plot plane
xx, yy = np.meshgrid(range(-5, 20), range(-10, 20))
zz = (5 - n[0]*xx - n[1]*yy) / n[2]
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

# Plot points
ax.scatter(*P, color='red', s=50)
ax.scatter(*Q, color='blue', s=50)

# Annotate points
ax.text(P[0], P[1], P[2], "P(-1,-5,-10)", color='red')
ax.text(Q[0], Q[1], Q[2], "Q(14,15,6)", color='blue')

# Draw distance vector PQ
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'r--')

# Annotate plane equation
ax.text(5, -8, (5 - n[0]*5 - n[1]*(-8))/n[2],
        r"$\vec{r}\cdot(\vec{i}-\vec{j}+\vec{k})=5$",
        color='black')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Line, Plane, and Distance between Points")

# Only legend for the line
ax.legend()
 plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/4.10.10/figs/q8.png")
plt.show()
