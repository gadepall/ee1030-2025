import numpy as np
import matplotlib.pyplot as plt

# Define points
A = np.array([2, -1, 3])
B = np.array([3, -5, 1])
C = np.array([-1, 11, 9])

# Step 1: Compute direction vectors
BA = B - A
CA = C - A

# Step 2: Form matrix with BA and CA as columns
M = np.column_stack((BA, CA))

print("Matrix M = [BA | CA]:\n", M)

# Step 3: Transpose (as per solution)
MT = M.T
print("\nTransposed matrix:\n", MT)

# Step 4: Row operation R2 = 3*R1 + R2
R = MT.copy().astype(float)
R[1] = 3 * R[0] + R[1]
print("\nAfter row operation (R2 = 3R1 + R2):\n", R)

# Step 5: Check rank
rank = np.linalg.matrix_rank(M)
print("\nRank =", rank)
if rank == 1:
    print("✅ The points are collinear.")
else:
    print("❌ The points are not collinear.")

# ----------------- Plotting -------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(A[0], A[1], A[2], color='red', label='A(2,-1,3)')
ax.scatter(B[0], B[1], B[2], color='blue', label='B(3,-5,1)')
ax.scatter(C[0], C[1], C[2], color='green', label='C(-1,11,9)')

# Plot line through A and B (which also contains C)
t = np.linspace(-2, 2, 100)
line = A.reshape(3,1) + t * BA.reshape(3,1)
ax.plot(line[0], line[1], line[2], 'k--', label='Line through A & B')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Collinearity of Points A, B, C")
ax.legend()

plt.show()

