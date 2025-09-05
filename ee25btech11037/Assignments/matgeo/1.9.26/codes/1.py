import ctypes
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL("./1.so")

# Define the function signature
lib.findK.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.findK.restype = ctypes.c_float

# Given points
px, py = 2, 4   # P(2,4)
ax = 5          # A(5,k)
by = 7          # B(k,7)

# Call the C function to get k
k = lib.findK(px, py, ax, by)

# Define points
P = (px, py)
A = (ax, k)
B = (k, by)

# Plot points
plt.figure(figsize=(6,6))
plt.scatter(*P, color="red", label=f"P{P}")
plt.scatter(*A, color="blue", label=f"A(5,{k:.2f})")
plt.scatter(*B, color="green", label=f"B({k:.2f},7)")

# Connect visually
plt.plot([P[0], A[0]], [P[1], A[1]], "b--", alpha=0.6)
plt.plot([P[0], B[0]], [P[1], B[1]], "g--", alpha=0.6)

# Formatting
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.title("Points P, A, and B")
plt.savefig("1.png")
plt.show()

