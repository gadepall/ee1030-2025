import numpy as np
import matplotlib.pyplot as plt
import os

# Given vectors (points)
A = np.array([2, 0])
B = np.array([4, 5])
C = np.array([1, 4])

# Method: area = 0.5 * |(B-A) x (C-A)|
AB = B - A
AC = C - A
cross_product = np.cross(AB, AC)
area = 0.5 * np.abs(cross_product)

print(f"Area of triangle ABC = {area}")

# -------- Plotting --------
plt.figure(figsize=(6,6))

# Plot points
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='black', zorder=5)
plt.text(A[0]+0.1, A[1]-0.2, 'A(2,0)', fontsize=12, color='black')
plt.text(B[0]+0.1, B[1], 'B(4,5)', fontsize=12, color='black')
plt.text(C[0]-0.8, C[1], 'C(1,4)', fontsize=12, color='black')

# Draw arrows for edges with different colors
plt.arrow(A[0], A[1], B[0]-A[0], B[1]-A[1],
          head_width=0.2, length_includes_head=True, color="red", linewidth=2)
plt.arrow(B[0], B[1], C[0]-B[0], C[1]-B[1],
          head_width=0.2, length_includes_head=True, color="green", linewidth=2)
plt.arrow(C[0], C[1], A[0]-C[0], A[1]-C[1],
          head_width=0.2, length_includes_head=True, color="blue", linewidth=2)

# Design
plt.title("Triangle ABC", fontsize=14, fontweight="bold")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_aspect('equal', adjustable='box')

# -------- Save to figures folder --------
save_path = "../figures"
os.makedirs(save_path, exist_ok=True)  # Create folder if not exists
plt.savefig(f"{save_path}/triangle.png", dpi=300, bbox_inches="tight")

plt.show()

