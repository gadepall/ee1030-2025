import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the points
P = np.array([4, 3, -5])
Q = np.array([-2, 1, 8])

# Generate line PQ
t = np.linspace(0, 1, 100)
line = np.outer(1-t, P) + np.outer(t, Q)

# Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot line PQ
ax.plot(line[:, 0], line[:, 1], line[:, 2], 'b-', label='$PQ$')

# Plot points P and Q
ax.scatter(P[0], P[1], P[2], color='red', s=60, label='P(4,3,-5)')
ax.scatter(Q[0], Q[1], Q[2], color='green', s=60, label='Q(-2,1,8)')

# Annotate points
ax.text(P[0]+0.3, P[1]+0.3, P[2], 'P(4,3,-5)', fontsize=10, color='red')
ax.text(Q[0]+0.3, Q[1]+0.3, Q[2], 'Q(-2,1,8)', fontsize=10, color='green')

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Title
ax.set_title("Line joining P(4,3,-5) and Q(-2,1,8)")

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# Save and show
plt.savefig("fig1.png", dpi=300, bbox_inches="tight")
plt.show()


