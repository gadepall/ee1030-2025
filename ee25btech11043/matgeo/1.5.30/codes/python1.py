import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_diameter = ctypes.CDLL("./code.so")

# Define the argument types and return type for the C function
lib_diameter.findOtherEndOfDiameter.argtypes = [
    ctypes.c_double,  # x1
    ctypes.c_double,  # y1
    ctypes.c_double,  # xc
    ctypes.c_double,  # yc
    ctypes.POINTER(ctypes.c_double), # x2
    ctypes.POINTER(ctypes.c_double)  # y2
]
lib_diameter.findOtherEndOfDiameter.restype = None

# Given coordinates
x1_given, y1_given = 2.0, 3.0  # One end of the diameter
xc_given, yc_given = -2.0, 5.0  # Center of the circle

# Create ctypes doubles to hold the results
x2_result = ctypes.c_double()
y2_result = ctypes.c_double()

# Call the C function to find the other end of the diameter
lib_diameter.findOtherEndOfDiameter(
    x1_given, y1_given,
    xc_given, yc_given,
    ctypes.byref(x2_result),
    ctypes.byref(y2_result)
)

x2_found = x2_result.value
y2_found = y2_result.value

print(f"The coordinates of the other end of the diameter are ({x2_found:.2f}, {y2_found:.2f})")

# Calculate the radius for plotting the circle
radius = np.sqrt((x1_given - xc_given)**2 + (y1_given - yc_given)**2)

# Generate points for the circle
theta = np.linspace(0, 2 * np.pi, 200)
circle_x = xc_given + radius * np.cos(theta)
circle_y = yc_given + radius * np.sin(theta)

# Plotting
plt.figure(figsize=(8, 8))

# Plot the circle
plt.plot(circle_x, circle_y, 'b-', label='Circle')

# Plot the given diameter end
plt.scatter(x1_given, y1_given, color='red', s=100, zorder=5, label='End 1 (2,3)')
plt.annotate(f'({x1_given},{y1_given})', (x1_given, y1_given), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the center
plt.scatter(xc_given, yc_given, color='green', s=100, zorder=5, label='Center (-2,5)')
plt.annotate(f'({xc_given},{yc_given})', (xc_given, yc_given), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the calculated other end of the diameter
plt.scatter(x2_found, y2_found, color='purple', s=100, zorder=5, label=f'End 2 ({x2_found:.2f},{y2_found:.2f})')
plt.annotate(f'({x2_found:.2f},{y2_found:.2f})', (x2_found, y2_found), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the diameter line
plt.plot([x1_given, x2_found], [y1_given, y2_found], 'r--', label='Diameter')

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Circle and its Diameter')
plt.grid(True)
plt.legend()
plt.show()
