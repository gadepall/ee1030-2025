import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#L1
A_start = np.array([1, 1, 0], dtype=np.float64)  # Point A in L1
m1 = np.array([2, -1, 1], dtype=np.float64)      # Direction vector of L1

# L2
B_start = np.array([2, 1, -1], dtype=np.float64) # Point B in L2
m2 = np.array([3, -5, 2], dtype=np.float64)      # Direction vector of L2

#Parameters for the closest points
k1_closest = 25/59
k2_closest = 7/59

#Closest points on the lines
point_A = A_start + k1_closest * m1   # Point on L1
point_B = B_start + k2_closest * m2   # Point on L2

# Shortest distance
shortest_dist = np.linalg.norm(point_B - point_A)


# Generate points for plotting
kappa_range = np.linspace(-3, 3, 100)
mu_range = np.linspace(-3, 3, 100)

L1_points = np.array([A_start + k * m1 for k in kappa_range])
L2_points = np.array([B_start + k * m2 for k in mu_range])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(L1_points[:,0], L1_points[:,1], L1_points[:,2], 'b', label='L1')
ax.plot(L2_points[:,0], L2_points[:,1], L2_points[:,2], 'orange', label='L2')

# Plot shortest distance part
ax.plot([point_A[0], point_B[0]],
        [point_A[1], point_B[1]],
        [point_A[2], point_B[2]], 'g', linewidth=2, label='Normal')

# Mark points A and B
ax.scatter(*point_A, color='b')
ax.scatter(*point_B , color='orange')
ax.text(*point_A + 0.5, "A", fontsize=10, color='b')
ax.text(*point_B - 1.0, "B", fontsize=10, color='orange')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=25, azim =75)
ax.legend()
ax.set_title("Shortest Distance between Skew Lines")
plt.savefig("fig.png", dpi=300)
plt.show()
