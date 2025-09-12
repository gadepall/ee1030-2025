import ctypes
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./triangle_area.so")

# Define the argument and return types
lib.triangle_area.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double]
lib.triangle_area.restype = ctypes.c_double

# Triangle vertices
A = (5, 2)
B = (4, 7)
C = (7, -4)

# Call the C function
area = lib.triangle_area(A[0], A[1], B[0], B[1], C[0], C[1])
print("Area of triangle ABC =", area)

# ---- Plotting ----
x_vals = [A[0], B[0], C[0], A[0]]
y_vals = [A[1], B[1], C[1], A[1]]

plt.plot(x_vals, y_vals, 'b-', linewidth=2, label="Triangle ABC")
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')

# Annotate points
plt.text(A[0], A[1], " A"+str(A))
plt.text(B[0], B[1], " B"+str(B))
plt.text(C[0], C[1], " C"+str(C))

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title(f"Triangle ABC (Area = {area})")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/2.6.25/figs/2.6.25.png")
plt.show()
