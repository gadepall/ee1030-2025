import numpy as np
import matplotlib.pyplot as plt

# Example vectors
a = np.array([1.0, 0.0])
b = np.array([0.6, 0.8])

# Gram matrix
c = np.dot(a, b)
G = np.array([[1, c],
              [c, 1]])

# Eigen decomposition
eigvals, eigvecs = np.linalg.eig(G)
idx = np.argmax(eigvals)
M = np.sqrt(eigvals[idx])
coeff = eigvecs[:, idx]

# Construct OP
OP = coeff[0]*a + coeff[1]*b
u = OP / np.linalg.norm(OP)
P = u * M

print("Pure Python:")
print("M =", M)
print("u =", u)

# Plot
O = np.array([0.0, 0.0])

plt.plot([O[0], P[0]], [O[1], P[1]], 'b-', label="Vector OP")
plt.scatter(*O, color="red", s=100, label="O(0,0)")
plt.scatter(*P, color="green", s=100, label=f"P({P[0]:.2f},{P[1]:.2f})")
plt.scatter(*u, color="purple", marker="*", s=200, label=f"u({u[0]:.2f},{u[1]:.2f})")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.title("Figure")
plt.grid(True)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/2.10.56/figs/figure1.png")
plt.show()
