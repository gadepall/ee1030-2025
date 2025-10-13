import numpy as np
import matplotlib.pyplot as plt

# Input values
x1, y1 = 60, 3
x2, y2 = 40, -6
y3 = -52

# Compute 'a' directly in Python
u1, u2 = (x2 - x1), (y2 - y1)
lambda_val = (y3 - y1) / u2
a = x1 + lambda_val * u1
print("Value of a =", a)

# Define points
A = np.array([x1, y1])
B = np.array([x2, y2])
C = np.array([a, y3])

# Plot points
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color="blue")

# Add labels near each point
plt.text(A[0] + 1, A[1] + 1, "A(60, 3)", fontsize=10, color="black")
plt.text(B[0] + 1, B[1] + 1, "B(40, -6)", fontsize=10, color="black")
plt.text(C[0] + 1, C[1] + 1, f"C({a:.2f}, -52)", fontsize=10, color="black")

# Plot line
plt.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], linestyle="--", color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Collinear Points")
plt.grid(True)
plt.show()
