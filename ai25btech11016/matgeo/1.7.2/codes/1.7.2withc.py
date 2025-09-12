import ctypes
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./collinear.so")
lib.is_collinear.argtypes = [ctypes.c_int]
lib.is_collinear.restype = ctypes.c_bool

# Points
O = (0, 0)
A = (1, 2)
a = 3   # try changing this value
C = (a, 6)

# Check collinearity using C function
print("Collinear?", lib.is_collinear(a))

# Plot points
plt.figure(figsize=(6,6))
plt.scatter(*O, color='black', label="O(0,0)")
plt.scatter(*A, color='red', label="A(1,2)")
plt.scatter(*C, color='blue', label=f"C({a},6)")

# If collinear, draw line through O, A, C
if lib.is_collinear(a):
    plt.plot([O[0], A[0], C[0]], [O[1], A[1], C[1]], 'g--', label="Collinear line")
else:
    # If not collinear, just connect O-A and O-C separately
    plt.plot([O[0], A[0]], [O[1], A[1]], 'r--')
    plt.plot([O[0], C[0]], [O[1], C[1]], 'b--')

# Formatting
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Collinearity Check of A, O, and C")
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/1.2.24/figs/1.7.2.png)
plt.show()
