import ctypes
import os
import matplotlib.pyplot as plt

# Load compiled shared library from code4.c
if os.name == "nt":   # Windows
    lib = ctypes.CDLL("./code4.dll")
else:                 # Linux/macOS
    lib = ctypes.CDLL("./code4.so")

# Define C function signature
lib.solve_k.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.solve_k.restype = None

# Prepare array for results
results = (ctypes.c_double * 2)()
lib.solve_k(results)

# Extract values of k
k1, k2 = results[0], results[1]
print(f"Possible values of k: {k1:.2f}, {k2:.2f}")

# Pick valid solution (k > 0)
k = k1 if k1 > 0 else k2
print(f"Chosen k = {k:.2f}")

# Define triangle vertices
A = (-2, 6)
B = (2 * k, 4)
C = (2 * k + 1, 10)

# Plot triangle
plt.figure(figsize=(7,7))
plt.plot([A[0], B[0], C[0], A[0]],
         [A[1], B[1], C[1], A[1]],
         'b-', linewidth=2)

# Plot vertices as red points
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]],
            color='red', s=80, zorder=5)

# Annotate vertices with coordinates
plt.text(A[0]+0.2, A[1]+0.2, f"A{A}", fontsize=12)
plt.text(B[0]+0.2, B[1]-0.4, f"B{B}", fontsize=12)
plt.text(C[0]+0.2, C[1]+0.2, f"C{C}", fontsize=12)

plt.title(f"Triangle with k = {k:.2f}")
plt.grid(True)
plt.axis("equal")

# Save as fig4.png
filename = "fig4.png"
plt.savefig(filename, dpi=200)
print(f"Figure saved as {filename}")

# Show the figure
plt.show()
