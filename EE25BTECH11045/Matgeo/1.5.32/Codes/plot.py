import matplotlib.pyplot as plt
import numpy as np

# Points
A = (1, -3)
B = (17/8, 0)
C = (4, 5)

# Plot points
plt.figure(figsize=(6,6))
plt.scatter(*A, color="red", label="A(1, -3)")
plt.scatter(*B, color="blue", label="B(17/8, 0)")
plt.scatter(*C, color="green", label="C(4, 5)")

# Connect points with lines
x_vals = [A[0], B[0], C[0], A[0]]
y_vals = [A[1], B[1], C[1], A[1]]
plt.plot(x_vals, y_vals, linestyle="--", color="black")

# Add text labels at coordinates
plt.text(A[0]+0.1, A[1]-0.3, "A(1, -3)", fontsize=10, color="red")
plt.text(B[0]+0.1, B[1]-0.3, "B(17/8, 0)", fontsize=10, color="blue")
plt.text(C[0]+0.1, C[1]+0.3, "C(4, 5)", fontsize=10, color="green")

# Labels and grid
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.title("Triangle ABC with Coordinates")

plt.show()