import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

# Define points
A = np.array([1, 2, 3])
B = np.array([4, 5, 7])
C = np.array([-4, 3, -6])
D = np.array([2, 9, 2])

# Direction vectors
BA = B - A
DC = D - C

print("Vector B-A:", BA)
print("Vector D-C:", DC)

# Compute angle
dot_product = np.dot(BA, DC)
norms = np.linalg.norm(BA) * np.linalg.norm(DC)
cos_theta = dot_product / norms
theta = np.degrees(np.arccos(cos_theta))

print("cos(theta) =", cos_theta)
print("Angle between AB and CD =", theta, "degrees")

# ---- Plotting ----
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='red', s=50, label='A(1,2,3)')
ax.scatter(*B, color='blue', s=50, label='B(4,5,7)')
ax.scatter(*C, color='green', s=50, label='C(-4,3,-6)')
ax.scatter(*D, color='purple', s=50, label='D(2,9,2)')

# Plot lines AB and CD
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='red', label='Line AB')
ax.plot([C[0], D[0]], [C[1], D[1]], [C[2], D[2]], color='green', label='Line CD')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lines AB and CD in 3D')
ax.legend()

# ---- Save into figs/fig1.png ----
os.makedirs("figs", exist_ok=True)  # create folder if it doesn't exist
plt.savefig("figs/fig1.png", dpi=300)
print(" Plot saved as figs/fig1.png")
