import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
handc = ctypes.CDLL("./func.so")

# Define argument and return types for the C function
handc.triangle_area.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # A
    ctypes.POINTER(ctypes.c_double),  # B
    ctypes.POINTER(ctypes.c_double)   # C
]
handc.triangle_area.restype = ctypes.c_double

# Convert numpy arrays to C pointers
def np_to_c(arr):
    return arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Fixed point A
A = np.array([1.0, -1.0], dtype=np.float64)

# k values we found
k_vals = [3.0, -9.0/2.0]

plt.figure(figsize=(6,6))

for k in k_vals:
    # Define points
    B = np.array([-4.0, 2.0*k], dtype=np.float64)
    C = np.array([-k, -5.0], dtype=np.float64)
    
    # Call the C function for area
    area = handc.triangle_area(np_to_c(A), np_to_c(B), np_to_c(C))
    print(f"k = {k}, area = {area}")
    
    # Plot triangle
    x_coords = [A[0], B[0], C[0], A[0]]
    y_coords = [A[1], B[1], C[1], A[1]]
    plt.plot(x_coords, y_coords, marker='o', label=f"k={k}")
    
    # Plot points with labels
    plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], s=50)
    plt.annotate("A(1,-1)", (A[0], A[1]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f"B(-4,{2*k:.1f})", (B[0], B[1]), textcoords="offset points", xytext=(0,10))
    plt.annotate(f"C({-k:.1f},-5)", (C[0], C[1]), textcoords="offset points", xytext=(0,-15))

plt.xlabel("x")
plt.ylabel("y")
plt.title("Triangles (Python + C area function)")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/triangle_area_c.png")
plt.show()

