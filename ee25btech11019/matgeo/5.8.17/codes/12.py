import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled shared library
lib = ctypes.CDLL('./line_intersection.so')

# Define the argument types for the C function
lib.findIntersection.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

# Define the two lines:
# 11x - 9y = -4
# 6x - 5y = -3

# Prepare variables to store results
x = ctypes.c_double()
y = ctypes.c_double()

# Call the C function
lib.findIntersection(11, -9, -4, 6, -5, -3, ctypes.byref(x), ctypes.byref(y))

# Get results from C function
x_int = x.value
y_int = y.value

print(f"Intersection point: ({x_int:.2f}, {y_int:.2f})")

# ---- Plotting the two lines ----
x_vals = np.linspace(-10, 10, 100)

# Equation form: y = (a*x - c)/b
y1 = (11*x_vals + 4)/9
y2 = (6*x_vals + 3)/5

plt.plot(x_vals, y1, label='11x - 9y = -4', color='blue')
plt.plot(x_vals, y2, label='6x - 5y = -3', color='red')

# Plot intersection point
plt.scatter(x_int, y_int, color='green', s=80, label=f'Intersection ({x_int:.2f}, {y_int:.2f})')

# Labeling
plt.title("Intersection of Two Lines")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)

# Highlight intersection point
plt.text(x_int, y_int, f"({x_int:.2f}, {y_int:.2f})", fontsize=12, ha='left', va='bottom', color='green')

# Show the plot
plt.show()