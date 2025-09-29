import numpy as np
import matplotlib.pyplot as plt

# Points as vectors
A = np.array([0, 5])
B = np.array([-5, 0])

# Distance using vector norm: ||B - A||
d = np.linalg.norm(B - A)
print("Distance ||B - A|| =", d)

# Plot
plt.scatter([A[0], B[0]], [A[1], B[1]], s=60)
plt.plot([A[0], B[0]], [A[1], B[1]], linewidth=2)

# Labels
plt.annotate("A(0, 5)", A + [0.2, 0.2])
plt.annotate("B(-5, 0)", B + [0.2, 0.2])

# Formatting
plt.title(f"Distance ||B - A|| = {d:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

# Save + show
import os

# Build the path: one folder out (..), then into figures/
save_path = os.path.join("..", "figures", "distance.png")

plt.savefig(save_path, dpi=150)

plt.show()
