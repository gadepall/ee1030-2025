import numpy as np
import matplotlib.pyplot as plt

# Define points A, B, C, D
A = np.array([1, 1, 1])
B = np.array([2, 5, 0])
C = np.array([3, 2, -3])
D = np.array([1, -6, -1])

# Compute vectors AB and CD
AB = B - A
CD = D - C

# Shift CD so its tail is at A (collinearity check)
CD_shifted_start = A
CD_shifted_end = A + CD

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original vectors
ax.quiver(A[0], A[1], A[2], AB[0], AB[1], AB[2], color='b', arrow_length_ratio=0.1, label="AB")
ax.quiver(C[0], C[1], C[2], CD[0], CD[1], CD[2], color='g', arrow_length_ratio=0.1, label="CD")

# Shifted CD (with arrow head, dotted style)
ax.quiver(CD_shifted_start[0], CD_shifted_start[1], CD_shifted_start[2],
          CD[0], CD[1], CD[2], color='r', linestyle="dashed",
          arrow_length_ratio=0.1, label="Shifted CD")

# Points
ax.scatter(*A, color='b')
ax.text(*A, "A")
ax.scatter(*B, color='b')
ax.text(*B, "B")
ax.scatter(*C, color='g')
ax.text(*C, "C")
ax.scatter(*D, color='g')
ax.text(*D, "D")

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title("AB and CD (Shifted CD from A with arrow head)")
plt.savefig("collinear_vectors_shifted.png", dpi=300)
plt.show()

