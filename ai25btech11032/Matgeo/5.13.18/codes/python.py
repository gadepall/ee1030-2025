import numpy as np
import matplotlib.pyplot as plt

# ---- Set k(solving with k as variable requires some concepts like nullspace which aren't taught yet) ----
k = 11.0   # change this to any real value

# ---- Build augmented matrix ----
A = np.array([
    [1, k,  3, 0],
    [3, k, -2, 0],
    [2, 4, -3, 0]
], dtype=float)

print("Original augmented matrix:")
print(A, "\n")

# ---- Row reduction ----
# Step 1: eliminate below pivot (0,0)
if A[0,0] != 0:
    A[1] = A[1] - (A[1,0]/A[0,0])*A[0]
    A[2] = A[2] - (A[2,0]/A[0,0])*A[0]

# Step 2: eliminate below pivot (1,1)
if A[1,1] != 0:
    A[2] = A[2] - (A[2,1]/A[1,1])*A[1]

print("Row reduced matrix:")
print(A, "\n")

# ---- Check rank ----
rank = np.linalg.matrix_rank(A[:,:3])
print("rank =", rank)

if rank == 3:
    print("Only trivial solution.")
else:
    # For k=11, reduced system gives:
    # 2y + z = 0 -> z = -2y
    # x + 11y + 3z = 0 -> x = -5y
    y = 1
    x = -5*y
    z = -2*y
    solution_vec = np.array([x,y,z], dtype=float)
    print("Solution vector:", solution_vec)

    ratio = (x*z)/(y*y)
    print("xz / y^2 =", ratio)

    # ---- Plot the solution line ----
    t = np.linspace(-2, 2, 200)
    line = np.outer(t, solution_vec)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(line[:,0], line[:,1], line[:,2], 'b-')
    ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
    ax.set_title(f"Solution line for k={k}")
    plt.savefig("newsolvek.png")
    plt.show()

