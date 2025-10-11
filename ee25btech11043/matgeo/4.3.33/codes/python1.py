import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_line = ctypes.CDLL("./code6.so")

# Define the argument types and return type for the C function
lib_line.findIntercepts.argtypes = [
    ctypes.c_double,  # xm (midpoint x-coordinate)
    ctypes.c_double,  # ym (midpoint y-coordinate)
    ctypes.POINTER(ctypes.c_double), # a (x-intercept)
    ctypes.POINTER(ctypes.c_double)  # b (y-intercept)
]
lib_line.findIntercepts.restype = None

# Given midpoint coordinates
xm_given, ym_given = 3.0, 2.0  # Midpoint of the line segment

# Create ctypes doubles to hold the results for 'a' and 'b'
a_result = ctypes.c_double()
b_result = ctypes.c_double()

# Call the C function to find the intercepts
lib_line.findIntercepts(
    xm_given, ym_given,
    ctypes.byref(a_result),
    ctypes.byref(b_result)
)

a_intercept = a_result.value
b_intercept = b_result.value

print(f"Given midpoint: ({xm_given:.2f}, {ym_given:.2f})")
print(f"The x-intercept (a) is: {a_intercept:.2f}")
print(f"The y-intercept (b) is: {b_intercept:.2f}")

# The equation of the line is x/a + y/b = 1
# Which can be rewritten as: b*x + a*y = a*b
# Or in standard form: b*x + a*y - a*b = 0

# For plotting, let's express y in terms of x:
# y = (-b/a) * x + b
slope = -b_intercept / a_intercept
y_intercept_calc = b_intercept

print(f"The equation of the line is: {b_intercept:.0f}x + {a_intercept:.0f}y = {a_intercept * b_intercept:.0f}")

# Plotting the line and intercepts
plt.figure(figsize=(8, 8))

# Generate points for the line
x_vals = np.linspace(-1, 7, 400)
y_vals = slope * x_vals + y_intercept_calc
plt.plot(x_vals, y_vals, 'b-', label=f'Line: {int(b_intercept)}x + {int(a_intercept)}y = {int(a_intercept * b_intercept)}')

# Plot the x-intercept
plt.scatter(a_intercept, 0, color='red', s=100, zorder=5, label=f'X-intercept ({a_intercept:.0f}, 0)')
plt.annotate(f'({a_intercept:.0f}, 0)', (a_intercept, 0), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the y-intercept
plt.scatter(0, b_intercept, color='green', s=100, zorder=5, label=f'Y-intercept (0, {b_intercept:.0f})')
plt.annotate(f'(0, {b_intercept:.0f})', (0, b_intercept), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the midpoint
plt.scatter(xm_given, ym_given, color='purple', s=100, zorder=5, label=f'Midpoint ({xm_given:.0f}, {ym_given:.0f})')
plt.annotate(f'({xm_given:.0f}, {ym_given:.0f})', (xm_given, ym_given), textcoords="offset points", xytext=(5,5), ha='left')

plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Equation of a Line with Given Midpoint of Intercepts')
plt.grid(True)
plt.legend()
plt.xlim(min(0, a_intercept) - 1, max(0, a_intercept) + 1)
plt.ylim(min(0, b_intercept) - 1, max(0, b_intercept) + 1)
plt.show()
