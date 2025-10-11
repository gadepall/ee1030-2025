import ctypes
import matplotlib.pyplot as plt
import numpy as np
import os

# --- 1. Load the Shared Library
LIB_NAME = '1.so'
try:
    lib_path = os.path.join(os.getcwd(), LIB_NAME)
    lib = ctypes.CDLL(lib_path)
    print(f"Successfully loaded '{LIB_NAME}'")
except OSError as e:
    print(f"Error: Could not load the shared library '{LIB_NAME}'.")
    print(f"Details: {e}")
    print("Please make sure you have compiled your C code and the .so file is in the correct directory.")
    exit()


# --- 2. Define the Function Signature (FIXED) ---
# Define the argument types for the C function
lib.perpendicularLine.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int,
                                  ctypes.POINTER(ctypes.c_int),
                                  ctypes.POINTER(ctypes.c_int),
                                  ctypes.POINTER(ctypes.c_int)]

# Define the return type. Assuming the C function returns 'void'.
# This is a critical step to prevent unexpected errors.
lib.perpendicularLine.restype = None


# --- 3. Prepare Inputs and Call C Function ---
# Inputs: line y = x → x - y = 0 → (a=1, b=-1, c=0), point (3,2)
a, b, c = 1, -1, 0
x0, y0 = 3, 2

# Prepare output variables to be passed by reference
A = ctypes.c_int()
B = ctypes.c_int()
C = ctypes.c_int()

# Call the C function
lib.perpendicularLine(a, b, c, x0, y0,
                      ctypes.byref(A), ctypes.byref(B), ctypes.byref(C))

print("Equation of perpendicular line: {}x + {}y + {} = 0".format(A.value, B.value, C.value))


# --- 4. Plotting Section (IMPROVED) ---
# Original line: y = x
x_vals = np.linspace(0, 6, 100)
y_given = x_vals

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_given, 'r--', label="Given line y = x")

# Plot point
plt.scatter(x0, y0, color='black', zorder=5) # zorder keeps point on top
plt.text(x0 + 0.1, y0 + 0.1, f"Point({x0},{y0})", fontsize=10)

# Check for vertical lines to avoid a division-by-zero error.
if B.value != 0:
    # Perpendicular line: A*x + B*y + C = 0 -> y = (-A*x - C)/B
    y_perp = (-A.value * x_vals - C.value) / B.value
    plt.plot(x_vals, y_perp, 'b-', label=f"{A.value}x + {B.value}y + {C.value} = 0")
else: # The line is vertical (Ax + C = 0)
    x_perp = -C.value / A.value
    plt.axvline(x=x_perp, color='b', linestyle='-', label=f"{A.value}x + {C.value} = 0")
    print("The perpendicular line is a vertical line.")

plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Perpendicular Line Calculation")
plt.grid(True)
plt.axis("equal")
plt.savefig('perpendicular_line.png')
plt.show()
