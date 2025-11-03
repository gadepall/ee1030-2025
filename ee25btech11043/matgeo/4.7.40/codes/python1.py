import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib_perpendicular = ctypes.CDLL("./code7.so")

# Define the argument types and return type for the C function
lib_perpendicular.find_perpendicular_details.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # P(x0, y0, z0)
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # L(x1, y1, z1)
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # D(a, b, c)
    ctypes.POINTER(ctypes.c_double), # foot_x
    ctypes.POINTER(ctypes.c_double), # foot_y
    ctypes.POINTER(ctypes.c_double), # foot_z
    ctypes.POINTER(ctypes.c_double)  # distance
]
lib_perpendicular.find_perpendicular_details.restype = None

# Given point P
P_x, P_y, P_z = 2.0, 3.0, -8.0

# Given line: (4 - x)/2 = y/6 = (1 - z)/3
# Rewrite in standard form: (x - x1)/a = (y - y1)/b = (z - z1)/c
# (x - 4)/(-2) = (y - 0)/6 = (z - 1)/(-3)

# Point on the line L
L_x, L_y, L_z = 4.0, 0.0, 1.0

# Direction ratios of the line D
D_a, D_b, D_c = -2.0, 6.0, -3.0

# Create ctypes doubles to hold the results
foot_x_result = ctypes.c_double()
foot_y_result = ctypes.c_double()
foot_z_result = ctypes.c_double()
distance_result = ctypes.c_double()

# Call the C function
lib_perpendicular.find_perpendicular_details(
    P_x, P_y, P_z,
    L_x, L_y, L_z,
    D_a, D_b, D_c,
    ctypes.byref(foot_x_result),
    ctypes.byref(foot_y_result),
    ctypes.byref(foot_z_result),
    ctypes.byref(distance_result)
)

foot_x_found = foot_x_result.value
foot_y_found = foot_y_result.value
foot_z_found = foot_z_result.value
distance_found = distance_result.value

print(f"The foot of the perpendicular is ({foot_x_found:.2f}, {foot_y_found:.2f}, {foot_z_found:.2f})")
print(f"The perpendicular distance is {distance_found:.2f}")

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the given point P
ax.scatter(P_x, P_y, P_z, color='black', s=100, label=f'Point P ({P_x},{P_y},{P_z})')
ax.text(P_x, P_y, P_z, f'  P ', color='black')

# Plot the foot of the perpendicular F
ax.scatter(foot_x_found, foot_y_found, foot_z_found, color='red', s=100, label=f'Foot of Perpendicular F ({foot_x_found:.2f},{foot_y_found:.2f},{foot_z_found:.2f})')
ax.text(foot_x_found, foot_y_found, foot_z_found, f'  F  ', color='red')

# Plot the line
# Parameter t for the line equation
t = np.linspace(-5, 5, 100) # Extend the line for better visualization
line_x = L_x + t * D_a
line_y = L_y + t * D_b
line_z = L_z + t * D_c
ax.plot(line_x, line_y, line_z, color='green', label='Line L')

# Plot the perpendicular line segment PF
ax.plot([P_x, foot_x_found], [P_y, foot_y_found], [P_z, foot_z_found], color='purple', linestyle='--', label='Perpendicular PF')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Foot of Perpendicular and Perpendicular Distance in 3D')
ax.legend()
ax.grid(True)
plt.show()
