import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Load shared library ---
lib = ctypes.CDLL("./solver.so")

# Define ctypes type
Mat3x4 = (ctypes.c_double * 4) * 3
lib.row_reduce.argtypes = [Mat3x4]
lib.row_reduce.restype = None

# --- Step 1: Build augmented matrix with variable k ---
k = 11  # try different k values here
A4 = Mat3x4()
A4[0][:] = (1, k, 3, 0)
A4[1][:] = (3, k, -2, 0)
A4[2][:] = (2, 4, -3, 0)

print("Original augmented matrix:")
for row in A4:
    print([float(x) for x in row])

# --- Step 2: Row-reduce using C ---
lib.row_reduce(A4)

print("\nRow-reduced augmented matrix:")
reduced = np.array([[A4[i][j] for j in range(4)] for i in range(3)], dtype=float)
print(reduced)

# --- Step 3: Check rank (ignoring last column) ---
coeff_matrix = reduced[:, :3]
rank = np.linalg.matrix_rank(coeff_matrix)
print("\nRank of coefficient matrix =", rank)

if rank == 3:
    print("Only trivial solution.")
    exit()

# --- Step 4: Solve system (from reduced form) ---
# From reduced system when k=11:
# Row2: 2y + z = 0 -> z = -2y
# Row1: x + 11y + 3z = 0 -> x = -5y
solution_vec = np.array([-5.0, 1.0, -2.0])
print("Solution vector:", solution_vec)

# Ratio
x, y, z = solution_vec
ratio = (x * z) / (y * y)
print("xz / y^2 =", ratio)

# --- Step 5: Plot solution line ---
t_vals = np.linspace(-2, 2, 200)
points = t_vals[:, None] * solution_vec[None, :]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(points[:, 0], points[:, 1], points[:, 2], "b-", linewidth=2)

ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
ax.set_xlim([-12, 12]); ax.set_ylim([-3, 3]); ax.set_zlim([-6, 6])
ax.set_title("Solution Line: multiples of (-5, 1, -2)")
plt.savefig("solvek.png")
plt.show()

