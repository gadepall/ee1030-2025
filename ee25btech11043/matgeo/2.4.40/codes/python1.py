import ctypes
import math
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
lib_angle = ctypes.CDLL("./code3.so")

# Define the argument types and return type for the C function
lib_angle.findAngleBetweenLines.argtypes = [
    ctypes.c_double,  # m1
    ctypes.c_double,  # m2
    ctypes.POINTER(ctypes.c_double) # angle_degrees
]
lib_angle.findAngleBetweenLines.restype = None

# Line 1: y - sqrt(3)x - 5 = 0  =>  y = sqrt(3)x + 5
# Slope m1 = sqrt(3)
m1_given = math.sqrt(3)

# Line 2: sqrt(3)y - x + 6 = 0  => sqrt(3)y = x - 6 => y = (1/sqrt(3))x - 6/sqrt(3)
# Slope m2 = 1/sqrt(3)
m2_given = 1 / math.sqrt(3)

# Create a ctypes double to hold the result
angle_result = ctypes.c_double()

# Call the C function to find the angle
lib_angle.findAngleBetweenLines(
    m1_given, m2_given, ctypes.byref(angle_result)
)

angle_found = angle_result.value

print(f"The angle between the lines is {angle_found:.2f} degrees")

# --- Plotting the lines ---
# Generate x values
x_vals = np.linspace(-10, 10, 400)

# Calculate y values for Line 1: y = sqrt(3)x + 5
y1_vals = m1_given * x_vals + 5

# Calculate y values for Line 2: y = (1/sqrt(3))x - 6/sqrt(3)
y2_vals = m2_given * x_vals - 6 / math.sqrt(3)

plt.figure(figsize=(10, 8))

# Plot Line 1
plt.plot(x_vals, y1_vals, label=f'Line 1: y - $\\sqrt{{3}}$x - 5 = 0 (m={m1_given:.2f})', color='blue')

# Plot Line 2
plt.plot(x_vals, y2_vals, label=f'Line 2: $\\sqrt{{3}}$y - x + 6 = 0 (m={m2_given:.2f})', color='red')


x_intersect = (-6 - 5 * math.sqrt(3)) / 2
y_intersect = math.sqrt(3) * x_intersect + 5 # Using Line 1 equation to find y

plt.scatter(x_intersect, y_intersect, color='green', s=100, zorder=5, label='Intersection')

plt.annotate(
    f'({x_intersect:.2f}, {y_intersect:.2f})',
    xy=(x_intersect, y_intersect),
    xytext=(x_intersect + 1, y_intersect + 1), # Offset text for better readability
    fontsize=10,
    color='black'
)


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'Lines and the Angle Between Them ({angle_found:.2f} degrees)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.ylim(-10, 10) # Adjust y-limits for better viewing
plt.xlim(-10, 10) # Adjust x-limits for better viewing
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
