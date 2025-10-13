import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Load C library (mat.so must be compiled from your C code) ---
lib = ctypes.CDLL('./mat.so')

# Signature: void solve_system(float A[3][4])
MatrixAug3x4 = (ctypes.c_float * 4) * 3
lib.solve_system.argtypes = [(ctypes.c_float * 4) * 3]
lib.solve_system.restype = None

# Define system of equations
A = np.array([
    [4.0, 3.0, 2.0],
    [2.0, 4.0, 6.0],
    [6.0, 2.0, 3.0]
], dtype=np.float32)
b = np.array([60.0, 90.0, 70.0], dtype=np.float32)

# Augmented matrix for C
aug = np.hstack((A, b.reshape(3, 1))).astype(np.float32)
aug_ctypes = MatrixAug3x4(
    (ctypes.c_float * 4)(*aug[0]),
    (ctypes.c_float * 4)(*aug[1]),
    (ctypes.c_float * 4)(*aug[2]),
)

print("C function output:")
lib.solve_system(aug_ctypes)

# Solve in Python (to get numeric solution back for plotting)
sol = np.linalg.solve(A, b)  # [x, y, z]
print(f"\nIntersection point (x, y, z): ({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})")

# --- Plotting ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Axes ranges
x_vals = np.linspace(0, 15, 20)
y_vals = np.linspace(0, 15, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Plane equations
Z1 = (60 - 4*X - 3*Y) / 2
Z2 = (90 - 2*X - 4*Y) / 6
Z3 = (70 - 6*X - 2*Y) / 3

# Plot planes
plane1 = ax.plot_surface(X, Y, Z1, alpha=0.2, color='blue')
plane2 = ax.plot_surface(X, Y, Z2, alpha=0.2, color='yellow')
plane3 = ax.plot_surface(X, Y, Z3, alpha=0.2, color='cyan')

# Plot intersection point
ax.scatter(sol[0], sol[1], sol[2], color='white', s=100, label=f"Intersection ({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})")

# Labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Planes and Intersection Point")

# Annotate planes with equations
ax.text(10, 0, (60 - 4*10 - 3*0)/2 + 1, "4x + 3y + 2z = 60", color="red", fontsize=10)
ax.text(0, 10, (90 - 2*0 - 4*10)/6 + 1, "2x + 4y + 6z = 90", color="green", fontsize=10)
ax.text(10, 10, (70 - 6*10 - 2*10)/3 + 1, "6x + 2y + 3z = 70", color="blue", fontsize=10)

# Annotate intersection point
ax.text(sol[0], sol[1], sol[2]+0.5, f"({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})", color="black", fontsize=10)

ax.legend()
plt.savefig('1.png')
plt.show()

