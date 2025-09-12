import numpy as np
import matplotlib.pyplot as plt

# Points
A = np.array([-5, 1])
C = np.array([4, -2])

# We already found p = -1
p = -1
B = np.array([1, p])

# Form the matrix to verify collinearity
BA = np.array([1 - (-5), p - 1])  # [6, p-1]
CA = np.array([4 - (-5), -2 - 1]) # [9, -3]
M = np.column_stack((BA, CA))

print("Matrix M:\n", M)
print("Rank of M:", np.linalg.matrix_rank(M))

# Plot
x_vals = np.linspace(-6, 5, 100)  # x range for line
# Equation of line through A and C: y = mx + c
m = (C[1] - A[1]) / (C[0] - A[0])
c = A[1] - m * A[0]
y_vals = m * x_vals + c

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, 'b-', label="Line through A, B, C")

# Plot points
plt.scatter(A[0], A[1], color='r', label="A(-5,1)")
plt.scatter(B[0], B[1], color='g', label="B(1,-1)")
plt.scatter(C[0], C[1], color='m', label="C(4,-2)")

# Annotate points
plt.text(A[0]+0.2, A[1]+0.2, "A(-5,1)")
plt.text(B[0]+0.2, B[1]-0.3, "B(1,-1)")
plt.text(C[0]+0.2, C[1]+0.2, "C(4,-2)")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.title("Collinearity of Points A, B, C")
plt.show()
