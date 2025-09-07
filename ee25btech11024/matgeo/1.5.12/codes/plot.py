import numpy as np
import matplotlib.pyplot as plt

# Given points
A = np.array([-6, 10])
B = np.array([3, -8])
P = np.array([-4, 6])   # Found from calculation

# Plotting
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'g--', label="Line AB")
plt.scatter(*A, color="red")
plt.scatter(*B, color="blue")
plt.scatter(*P, color="black")

# Labels
plt.text(A[0], A[1]+0.5, "A(-6,10)", fontsize=10)
plt.text(B[0], B[1]-0.8, "B(3,-8)", fontsize=10)
plt.text(P[0], P[1]+0.5, "P(-4,6)", fontsize=10)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Point P dividing AB in 2:7")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("fig.png")
plt.show()
