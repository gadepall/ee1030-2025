import numpy as np
import matplotlib.pyplot as plt

# Points
O = np.array([0, 0])
A = np.array([1, 2])
C = np.array([3, 6])  # since a = 3

# Plot the points
plt.figure(figsize=(6,6))
plt.scatter(*O, color='black', label='O(0,0)')
plt.scatter(*A, color='red', label='A(1,2)')
plt.scatter(*C, color='blue', label='C(3,6)')

# Draw lines between them
plt.plot([O[0], A[0], C[0]], [O[1], A[1], C[1]], 'g--', label='Collinear line')

# Labels and formatting
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/1.2.24/figs/1.7.2.png")
plt.show()
