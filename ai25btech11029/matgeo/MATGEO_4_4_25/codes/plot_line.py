import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./libline_solver.so')

# Define the C struct LineEquation in Python
class LineEquation(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double)]

# Bind the C function signature
lib.get_horizontal_line_through_point.argtypes = [ctypes.c_double, ctypes.c_double]
lib.get_horizontal_line_through_point.restype = LineEquation

# Call the C function
line = lib.get_horizontal_line_through_point(2.0, -4.0)

# Print the result
print(f"Line equation from C: {line.a}x + {line.b}y + {line.c} = 0")

# Plot the line: y = -4
x = np.linspace(-10, 10, 400)
y = -line.c / line.b * np.ones_like(x)

plt.plot(x, y, label=f'{line.a}x + {line.b}y + {line.c} = 0', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Line Parallel to X-axis Through (2, -4)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

