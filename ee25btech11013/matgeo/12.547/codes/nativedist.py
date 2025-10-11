import numpy as np
import matplotlib.pyplot as plt

# Define vectors and point
u1 = np.array([1.0, 1.0, 0.0])
u2 = np.array([0.0, 1.0, 1.0])
P  = np.array([1.0, 1.0, 1.0])

# Stack u1 and u2 as columns to form U
U = np.column_stack((u1, u2))

# Compute projection coefficients: inv(U^T U) * U^T * P
coeff = np.linalg.inv(U.T @ U) @ (U.T @ P)

# Compute projection point
P_proj = U @ coeff

# Compute distance
distance = np.linalg.norm(P - P_proj)
print(f"Distance from P to plane: {distance:.6f}")
print(f"Projection point: {P_proj}")

# Create plane grid
s = np.linspace(-0.5, 2, 10)
t = np.linspace(-0.5, 2, 10)
S, T = np.meshgrid(s, t)
X = S*u1[0] + T*u2[0]
Y = S*u1[1] + T*u2[1]
Z = S*u1[2] + T*u2[2]

# Plotting
fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')

# Plane
ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.5)

# Original point
ax.scatter(*P, color='red', s=80, label='P = (1,1,1)')

# Projection point
ax.scatter(*P_proj, color='green', s=80)
ax.text(P_proj[0], P_proj[1], P_proj[2],
        f'({P_proj[0]:.2f}, {P_proj[1]:.2f}, {P_proj[2]:.2f})',
        color='green', fontsize=10, ha='left', va='bottom')

# Distance line
ax.plot([P[0], P_proj[0]], [P[1], P_proj[1]], [P[2], P_proj[2]], 'k--', label='Distance')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Distance from Point to Plane')
ax.legend()
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.547/figs/Figure_1.png")
plt.show()


