import numpy as np
import matplotlib.pyplot as plt

# Symbolic vectors (set a = 1, b = 1 for proportional plotting)
a, b = 1, 1

# Given position vectors
X = np.array([3*a, b])      # (3a, b)
Y = np.array([a, -3*b])     # (a, -3b)
k = 2                       # ratio 2:1 externally

# External division formula: Z = (kY - X) / (k - 1)
Z = (k*Y - X) / (k - 1)     # should give (-a, -7b)

# Plot
plt.figure(figsize=(6,6))
plt.plot([X[0], Y[0]], [X[1], Y[1]], 'b--', label='Line XY')
plt.scatter(*X, color='red', label='X (3a, b)')
plt.scatter(*Y, color='green', label='Y (a, -3b)')
plt.scatter(*Z, color='purple', label='Z (-a, -7b)')

# Annotate points
plt.text(X[0]+0.2, X[1], 'X(3a, b)', fontsize=11)
plt.text(Y[0]+0.2, Y[1], 'Y(a, -3b)', fontsize=11)
plt.text(Z[0]+0.2, Z[1], 'Z(-a, -7b)', fontsize=11)

# Axes styling
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.axis('equal')
plt.xlim(-8, 5)
plt.ylim(-8, 5)
plt.xlabel('a-axis')
plt.ylabel('b-axis')
plt.title('External Division of XY in Ratio 2:1 (in terms of a and b)')
plt.legend()

# Save figure
plt.savefig("external_division.png", dpi=300, bbox_inches='tight')
plt.show()

print("✅ Figure saved as 'external_division.png'")

