import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load C library
c_lib = ctypes.CDLL('./triangle.so')

# Set return types
c_lib.is_right_triangle.restype = ctypes.c_int
c_lib.is_isosceles.restype = ctypes.c_int

# Call C functions
is_right = c_lib.is_right_triangle()
is_iso = c_lib.is_isosceles()

print("Is the triangle right-angled?", "YES" if is_right else "NO")
print("Is the triangle isosceles?", "YES" if is_iso else "NO")

# Triangle vertices
A = np.array([-4, 0])
B = np.array([0, 3])
C = np.array([4, 0])

# Midpoints
x_mid = (A + B) / 2
y_mid = (B + C) / 2
z_mid = (A + C) / 2

# Plot triangle
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', linewidth=2)

# Plot vertices
plt.scatter(*A, color='red')
plt.scatter(*B, color='green')
plt.scatter(*C, color='blue')
plt.text(A[0]-0.6, A[1]-0.3, "A(-4,0)")
plt.text(B[0]+0.2, B[1], "B(0,3)")
plt.text(C[0]+0.2, C[1]-0.3, "C(4,0)")

# Plot midpoints
plt.scatter(*x_mid, color='orange')
plt.scatter(*y_mid, color='orange')
plt.scatter(*z_mid, color='orange')
plt.text(x_mid[0]-0.8, x_mid[1], f"({x_mid[0]}, {x_mid[1]})")
plt.text(y_mid[0]+0.2, y_mid[1], f"({y_mid[0]}, {y_mid[1]})")
plt.text(z_mid[0]+0.2, z_mid[1]-0.3, f"({z_mid[0]}, {z_mid[1]})")

# Draw medians
plt.plot([C[0], x_mid[0]], [C[1], x_mid[1]], 'r--')
plt.plot([A[0], y_mid[0]], [A[1], y_mid[1]], 'g--')
plt.plot([B[0], z_mid[0]], [B[1], z_mid[1]], 'b--')

plt.axis('equal')
plt.grid(True)
plt.title("Triangle ABC with Medians & Midpoints")
plt.show()
