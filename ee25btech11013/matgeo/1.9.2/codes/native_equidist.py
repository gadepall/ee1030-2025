import numpy as np
import matplotlib.pyplot as plt


A = np.array([-4, 0])
B = np.array([10, 0])


e1 = np.array([1, 0])


num = np.linalg.norm(A)**2 - np.linalg.norm(B)**2
den = 2 * np.dot(A - B, e1)
x = num / den


O = x * e1

print("Point equidistant from A and B on x-axis:", O)


plt.figure(figsize=(6,6))
plt.axhline(0, color='gray', linewidth=0.8)  # x-axis
plt.axvline(0, color='gray', linewidth=0.8)  # y-axis

# Plot points
plt.scatter(A[0], A[1], color='red', label='A (-4,0)')
plt.scatter(B[0], B[1], color='blue', label='B (10,0)')
plt.scatter(O[0], O[1], color='green', marker='*', s=150, label=f'O ({int(O[0])},0)')


plt.plot([A[0], O[0]], [A[1], O[1]], 'r--', linewidth=1)
plt.plot([B[0], O[0]], [B[1], O[1]], 'b--', linewidth=1)

plt.legend(loc="upper right")
plt.grid(True, linestyle='--', alpha=0.6)
plt.title("Equidistant Point on X-axis")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.savefig("/Users/bhargavkrish/Documents/ee1030-2025/ee25btech11013/matgeo/1.9.2/figs/Figure_1.png")
plt.show()

