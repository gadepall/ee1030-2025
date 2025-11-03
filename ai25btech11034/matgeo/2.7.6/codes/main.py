# main.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# Load C shared library
lib = ctypes.CDLL("./function.so")
lib.cross.argtypes = [ctypes.c_double * 2, ctypes.c_double * 2]
lib.cross.restype = ctypes.c_double

def cross(u, v):
    arr_u = (ctypes.c_double * 2)(*u)
    arr_v = (ctypes.c_double * 2)(*v)
    return lib.cross(arr_u, arr_v)

# Points
A = np.array([2, 0])
B = np.array([4, 5])
C = np.array([1, 4])

# Compute vectors AB and AC
AB = B - A
AC = C - A

# Call C function for cross product
cross_val = cross(AB, AC)

# Triangle area
area = abs(cross_val) / 2
print("Area of triangle:", area)

# Plotting
points = np.array([A, B, C, A])  # closed loop
colors = ['r', 'g', 'b']  # different colors for arrows

plt.figure(figsize=(6,6))
plt.scatter(points[:,0], points[:,1], color='black')

# Draw arrows between consecutive points
for i in range(3):
    plt.arrow(points[i,0], points[i,1],
              points[i+1,0]-points[i,0],
              points[i+1,1]-points[i,1],
              head_width=0.2, length_includes_head=True,
              color=colors[i], linestyle='-')

# Label points
plt.text(A[0], A[1]-0.3, "A(2,0)", fontsize=10, ha="center")
plt.text(B[0], B[1]+0.3, "B(4,5)", fontsize=10, ha="center")
plt.text(C[0], C[1]+0.3, "C(1,4)", fontsize=10, ha="center")

plt.axis("equal")
plt.grid(True)
plt.title(f"Triangle Area = {area:.2f}")

# Save to ../figures
save_path = os.path.join("..", "figures", "triangle.png")
plt.savefig(save_path, dpi=300)
plt.close()

