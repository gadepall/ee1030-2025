# main.py
import ctypes
import matplotlib.pyplot as plt

# Load shared object
lib = ctypes.CDLL('./libmidpoint.so')

# Define argument and return types
lib.midpoint.argtypes = [ctypes.c_double, ctypes.c_double,
                         ctypes.c_double, ctypes.c_double,
                         ctypes.POINTER(ctypes.c_double),
                         ctypes.POINTER(ctypes.c_double)]

# Input points A and B
x1, y1 = -1, 1
x2, y2 = 3, 3

# Output variables
mx = ctypes.c_double()
my = ctypes.c_double()

# Call C function
lib.midpoint(x1, y1, x2, y2, ctypes.byref(mx), ctypes.byref(my))

print(f"Midpoint of A and B: ({mx.value}, {my.value})")

# Points
A = (x1, y1)
B = (x2, y2)
M = (mx.value, my.value)
P = (0, 2)  # intersection with Y-axis

# Plot
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label="Line AB")
plt.plot([M[0],P[0]], [M[1],P[1]], 'b-', label="Line MP")
plt.scatter(*A, color='red', label="A(-1,1)")
plt.scatter(*B, color='green', label="B(3,3)")
plt.scatter(*M, color='purple', label=f"M{M}")
plt.scatter(*P, color='orange', label="P(0,2)")

plt.text(A[0]+0.08,A[1]+0.1,'A', color='red')
plt.text(B[0]-0.08,B[1]-0.1,'B', color='green')
plt.text(M[0]+0.08,M[1]+0.1,'M', color='purple')
plt.text(0+0.08,2+0.1,'P', color='orange')


# Draw perpendicular bisector line
plt.axvline(x=0, color='gray', linestyle='--', label="Y-axis")
plt.legend()
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Midpoint and Perpendicular Bisector Intersection")
plt.savefig("figure.png", dpi=150)
plt.show()

