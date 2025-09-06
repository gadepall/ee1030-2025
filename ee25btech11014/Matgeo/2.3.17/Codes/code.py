import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
c_lib = ctypes.CDLL('./triangle.so')

# Function signature
triangle_properties = c_lib.triangle_properties
triangle_properties.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # sides[3]
    ctypes.POINTER(ctypes.c_double)   # angles[3]
]
triangle_properties.restype = None

# Prepare arrays
sides = (ctypes.c_double * 3)()
angles = (ctypes.c_double * 3)()

# Call the C function
triangle_properties(sides, angles)

# Convert to Python lists
sides_py = [sides[i] for i in range(3)]
angles_py = [angles[i] for i in range(3)]

print(f"Sides (AB, BC, CA): {sides_py}")
print(f"Angles (A, B, C): {angles_py} (degrees)")

# --- Plotting ---
A = np.array([-4, 0])
B = np.array([0, 3])
C = np.array([4, 0])

plt.figure(figsize=(8,6))
x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]
plt.plot(x_coords, y_coords, 'b-', linewidth=2, label="Triangle ABC")

# Mark vertices
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color="red")
plt.text(A[0]-1, A[1]-0.3, f"A(-4,0)\n∠A≈{angles_py[0]:.2f}°", color="red")
plt.text(B[0]+0.2, B[1]+0.3, f"B(0,3)\n∠B≈{angles_py[1]:.2f}°", color="green")
plt.text(C[0]+0.4, C[1]-0.3, f"C(4,0)\n∠C≈{angles_py[2]:.2f}°", color="blue")

# Annotate side lengths at midpoints
midpoints = [
    ((A[0]+B[0])/2, (A[1]+B[1])/2, sides_py[0]),
    ((B[0]+C[0])/2, (B[1]+C[1])/2, sides_py[1]),
    ((C[0]+A[0])/2, (C[1]+A[1])/2, sides_py[2])
]
for (mx, my, d) in midpoints:
    plt.text(mx+0.2, my+0.2, f"{d:.2f}", fontsize=10, color="purple")

# Axis
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.axis('equal')
plt.grid(True)
plt.title("Triangle ABC with Sides and Angles (from C)")
plt.legend()
plt.savefig("triangle_matrix.png")
plt.show()
