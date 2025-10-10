import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Part 1: Symbolic solution using Sympy to get the transformation rule
A1, A2, A3, theta = sp.symbols('A1 A2 A3 theta')
A_vec = sp.Matrix([A1, A2, A3])
Rx = sp.Matrix([
    [1, 0, 0],
    [0, sp.cos(theta), sp.sin(theta)],
    [0, -sp.sin(theta), sp.cos(theta)]
])
Rx_pi_half = Rx.subs(theta, sp.pi/2)
A_prime_vec = Rx_pi_half * A_vec

# Part 2: Visualization with Matplotlib using arbitrary values

# Define arbitrary values for the original vector A
A_numerical = np.array([4, 7, 2])

# Calculate the components of the new vector A' using the derived rule
A_prime_numerical = np.array([
    A_numerical[0],
    A_numerical[2],
    -A_numerical[1]
])

# Print the original and resulting vectors
print(f"Original vector A = {A_numerical}")
print(f"Resulting vector A' = {A_prime_numerical}")

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the original vector A using quiver
ax.quiver(0, 0, 0, A_numerical[0], A_numerical[1], A_numerical[2],
          color='blue', length=np.linalg.norm(A_numerical),
          arrow_length_ratio=0.1, label='Original Vector A')
ax.text(A_numerical[0], A_numerical[1], A_numerical[2], '  A = ({}, {}, {})'.format(*A_numerical), color='blue', fontsize=12)

# Plot the transformed vector A' using quiver
ax.quiver(0, 0, 0, A_prime_numerical[0], A_prime_numerical[1], A_prime_numerical[2],
          color='red', length=np.linalg.norm(A_prime_numerical),
          arrow_length_ratio=0.1, label='Transformed Vector A\'')
ax.text(A_prime_numerical[0], A_prime_numerical[1], A_prime_numerical[2], "  A' = ({}, {}, {})".format(*A_prime_numerical), color='red', fontsize=12)

# Setting plot labels and limits
max_val = np.max(np.abs(np.concatenate((A_numerical, A_prime_numerical)))) * 1.2
ax.set_xlim([-1, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('Vector Transformation under Coordinate System Rotation', fontsize=16)

# Set the viewing angle
ax.view_init(elev=20, azim=30)
ax.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
