import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vectors
a = np.array([1, 1, 1])
b = np.array([0, 1, -1])

# Function to compute scalar triple product
def scalar_triple_product(lam):
    c = np.array([3 - 2*lam, lam, lam])
    return np.dot(np.cross(a, c), b)

# Brute-force loop to find lambda such that triple product ≈ 2
best_lambda = None
for lam in np.linspace(0, 2, 1000):  # Try 1000 values between 0 and 2
    result = scalar_triple_product(lam)
    if abs(result - 2) < 1e-5:
        best_lambda = lam
        break

# Compute c using best_lambda
c = np.array([3 - 2*best_lambda, best_lambda, best_lambda])

# Print results
print(f"Lambda = {best_lambda}")
print(f"Vector c = {c}")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
origin = [0, 0, 0]

# Plot vectors a, b, and c
ax.quiver(*origin, *a, color='red', label='a', linewidth=2)
ax.quiver(*origin, *b, color='green', label='b', linewidth=2)
ax.quiver(*origin, *c, color='blue', label='c', linewidth=2)

# Set plot limits
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors a, b, and c')
ax.legend()

plt.tight_layout()
plt.show()

