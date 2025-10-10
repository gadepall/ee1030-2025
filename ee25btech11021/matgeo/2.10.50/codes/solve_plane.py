import ctypes
import sympy as sp
import numpy as np

# --- 1. Load C library ---
lib = ctypes.CDLL("./plane_points.so")
lib.generate_plane_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
lib.generate_plane_points.restype = None

# --- 2. Symbolic variables ---
a, b, c = sp.symbols('a b c', positive=True)

# --- 3. Compute centroid symbolically ---
A = sp.Matrix([a, 0, 0])
B = sp.Matrix([0, b, 0])
C = sp.Matrix([0, 0, c])
D = (A + B + C)/3

# --- 4. Compute k symbolically ---
k = 1/D[0]**2 + 1/D[1]**2 + 1/D[2]**2

# --- 5. Apply plane condition: 1/a^2 + 1/b^2 + 1/c^2 = 1 ---
plane_condition = 1/a**2 + 1/b**2 + 1/c**2
k_final = k.subs(plane_condition, 1)

print("Centroid D =", D)
print("k in terms of a,b,c =", k)
print("Using plane condition 1/a^2 + 1/b^2 + 1/c^2 = 1")
print("Final k =", k_final)

# --- 6. Optional: Call C program to generate points numerically ---
# Here we must provide numeric values to C, just as placeholders
points_array = (ctypes.c_double * 9)()
lib.generate_plane_points(1.0, 1.0, 1.0, points_array)
A_num = np.array(points_array[0:3])
B_num = np.array(points_array[3:6])
C_num = np.array(points_array[6:9])

print("\nPoints from C code (numeric placeholders):")
print("A =", A_num)
print("B =", B_num)
print("C =", C_num)
