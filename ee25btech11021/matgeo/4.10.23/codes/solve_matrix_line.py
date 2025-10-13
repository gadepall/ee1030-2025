import ctypes
import numpy as np

# --- Step 0: Load C library ---
lib = ctypes.CDLL("./line_generator.so")
lib.generate_line_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                     ctypes.c_int, ctypes.c_int]

# --- Step 1: Matrix method to find required line ---
n1 = np.array([2, 1])
c1 = 5
n2 = np.array([1, 3])
c2 = -8
n3 = np.array([3, 4])  # line to be parallel

# Family of lines: N(lambda) = n1 + lambda*n2
# Parallel condition: N(lambda) = alpha * n3
# Solve for lambda:
lambda_val = 1  # from calculation

# Normal vector and constant of required line
N = n1 + lambda_val * n2
c = c1 + lambda_val * c2

print("Normal vector of required line:", N)
print("Constant term:", c)
print(f"Equation of line: {N[0]}x + {N[1]}y + {c} = 0\n")

# --- Step 2: Call C function to generate points ---
print("Points on the line:")
lib.generate_line_points(float(N[0]), float(N[1]), float(c), -5, 5)

