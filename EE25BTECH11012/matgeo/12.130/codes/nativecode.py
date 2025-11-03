import numpy as np
import matplotlib.pyplot as plt

# Define the matrix M
M = np.array([
    [0, 0, 1],
    [0, 0, 0],
    [-1, 0, 0]
])

# Compute eigenvalues
eigenvalues = np.linalg.eigvals(M)

# Print eigenvalues
print("Eigenvalues of M:", eigenvalues)

# Plot eigenvalues in the complex plane
plt.figure(figsize=(6, 6))
plt.scatter(eigenvalues.real, eigenvalues.imag, color='red', s=100, label='Eigenvalues')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.title('Eigenvalues in the Complex Plane')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.legend()
plt.show()