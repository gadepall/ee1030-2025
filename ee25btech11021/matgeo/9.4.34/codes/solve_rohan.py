import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL('./libpoints.so')

N = 100
x_line = np.zeros(N, dtype=np.double)
y_line = np.zeros(N, dtype=np.double)

# Set argument types
lib.generate_line.argtypes = [ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.c_int]
lib.generate_line.restype = None

# Call function
lib.generate_line(x_line.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                  y_line.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                  N)

print("Sample points from C library (line):")
for i in range(5):
    print(f"x={x_line[i]}, y={y_line[i]}")

# -----------------------------
# MATRIX METHOD SOLUTION
# -----------------------------
V = np.array([[0, 0.5],
              [0.5, 0]])
u = np.array([[1.5],
              [1.5]])
f = -351

h = np.array([[0],
              [26]])
m = np.array([[1],
              [1]])

mT_V_m = (m.T @ V @ m)[0,0]
Vh_plus_u = V @ h + u
mT_Vh_plus_u = (m.T @ Vh_plus_u)[0,0]
g_h = (h.T @ V @ h + 2*(u.T @ h) + f)[0,0]

a = mT_V_m
b = 2 * mT_Vh_plus_u
c = g_h

kappa = np.roots([a, b, c])

points = [h + k*m for k in kappa]

for pt in points:
    x_val = pt[0,0]
    y_val = pt[1,0]
    if x_val >= 0 and y_val >= 0:
        rohan_age = x_val
        mother_age = y_val

print(f"\nRohan's present age: {rohan_age} years")
print(f"Mother's present age: {mother_age} years")

# Save for plotting
np.savez("rohan_points.npz",
         x_line=x_line, y_line=y_line,
         rohan_age=rohan_age, mother_age=mother_age)

