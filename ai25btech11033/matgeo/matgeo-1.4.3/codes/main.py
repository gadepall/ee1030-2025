

import numpy as np
import matplotlib.pyplot as plt

# Define points
A = np.array([1/2, 3/2])
B = np.array([2, -5])
P = np.array([3/4, 5/12])

# Section formula ratio check
AP = np.linalg.norm(P - A)
PB = np.linalg.norm(B - P)
ratio = AP / PB

# Plotting
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Line AB')  # Line AB
plt.scatter(*A, color='blue', s=100, label='A(1/2, 3/2)')
plt.scatter(*B, color='green', s=100, label='B(2, -5)')
plt.scatter(*P, color='red', s=100, label='P(3/4, 5/12)')

# Annotating
plt.text(A[0]+0.1, A[1], 'A', fontsize=12, color='blue')
plt.text(B[0]+0.1, B[1], 'B', fontsize=12, color='green')
plt.text(P[0]+0.1, P[1], 'P', fontsize=12, color='red')

plt.title(f"Point P divides AB in ratio {AP:.2f}:{PB:.2f} ≈ 1:5")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
