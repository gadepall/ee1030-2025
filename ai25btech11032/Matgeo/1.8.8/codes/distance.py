import numpy as np
import matplotlib.pyplot as plt

# Points as vectors
A = np.array([0, 6])
B = np.array([0, -2])

# Distance using vector norm: ||B - A||
d = np.linalg.norm(B - A)
print("Distance ||B - A|| =", d)

# Plot
plt.scatter([A[0], B[0]], [A[1], B[1]], s=60)
plt.plot([A[0], B[0]], [A[1], B[1]], linewidth=2)

# Labels
plt.annotate("A(0, 6)", A + [0.2, 0.2])
plt.annotate("B(0, -2)", B + [0.2, -0.5])

# Formatting
plt.title(f"Distance ||B - A|| = {d:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

# Save + show
plt.savefig("distancenew.png", dpi=150)
plt.show()
