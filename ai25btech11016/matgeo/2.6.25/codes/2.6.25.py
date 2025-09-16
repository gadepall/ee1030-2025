import numpy as np
import matplotlib.pyplot as plt

# Given points
A = np.array([5, 2])
B = np.array([4, 7])
C = np.array([7, -4])

# Compute area using determinant formula
area = 0.5 * abs(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]))
print("Area of triangle:", area)

# Plot triangle
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', linewidth=2)
plt.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='skyblue', alpha=0.4)

# Mark points
plt.scatter(*A, color='r')
plt.text(A[0]+0.2, A[1], "A(5,2)", fontsize=10)
plt.scatter(*B, color='r')
plt.text(B[0]+0.2, B[1], "B(4,7)", fontsize=10)
plt.scatter(*C, color='r')
plt.text(C[0]+0.2, C[1], "C(7,-4)", fontsize=10)

# Axis setup
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect("equal")
plt.title(f"Triangle ABC, Area = {area}")
plt.grid(True)
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/2.6.25/figs/2.6.25.png")
plt.show()
