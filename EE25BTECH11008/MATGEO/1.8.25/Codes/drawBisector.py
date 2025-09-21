import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./info.so")

# Define arg + return types
lib.perpendicular_bisector.argtypes = (ctypes.c_double, ctypes.c_double,
                                       ctypes.c_double, ctypes.c_double,
                                       ctypes.POINTER(ctypes.c_double),
                                       ctypes.POINTER(ctypes.c_double),
                                       ctypes.POINTER(ctypes.c_double))
lib.perpendicular_bisector.restype = None

# Inputs
A = (7.0, 1.0)
B = (3.0, 5.0)

# Prepare outputs
a = ctypes.c_double()
b = ctypes.c_double()
c = ctypes.c_double()

# Call C function
lib.perpendicular_bisector(A[0], A[1], B[0], B[1],
                           ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))

print(f"Equation: {a.value:.2f}x + {b.value:.2f}y + {c.value:.2f} = 0")

# Plot
x = np.linspace(0, 10, 100)
y = (-a.value * x - c.value) / b.value

plt.plot(x, y, 'k-', label='Bisector')
plt.text(A[0] + 0.3, A[1], r'A (7,1)', fontsize=12, color='red')
plt.text(B[0] + 0.3, B[1], r'B (3,5)', fontsize=12, color='blue')
plt.text(7, ( -a.value*6 - c.value)/b.value + 0.3,
         f"{a.value:.0f}x + {b.value:.0f}y + {c.value:.0f} = 0",
         fontsize=12, color="black")
plt.scatter(*A, color='red', label='A (7,1)')
plt.scatter(*B, color='blue', label='B (3,5)')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.legend()
plt.show()
