import matplotlib.pyplot as plt
import numpy as np
import sympy

# --- Part 1: Solve for the angles using SymPy ---

# Define the angles as symbolic variables
A, B, C = sympy.symbols('A B C')

# Define the equations based on the problem statement
# Equation 1: The sum of angles in a triangle is 180 degrees
eq1 = sympy.Eq(A + B + C, 180)

# Equation 2: From the relation C = 3B
eq2 = sympy.Eq(C, 3 * B)

# Equation 3: From the relation 3B = 2(A + B)
eq3 = sympy.Eq(3 * B, 2 * (A + B))

# Solve the system of equations
solution = sympy.solve((eq1, eq2, eq3), (A, B, C))

# Convert SymPy Integer types to standard Python int types
angle_A_deg = int(solution[A])
angle_B_deg = int(solution[B])
angle_C_deg = int(solution[C])

print("--- Calculated Angles ---")
print(f"Angle A: {angle_A_deg}°")
print(f"Angle B: {angle_B_deg}°")
print(f"Angle C: {angle_C_deg}°")
print("-------------------------")


# --- Part 2: Construct and plot the triangle ---

# Set vertex coordinates to build the triangle
vert_A = np.array([0, 0])
base_length = 10
vert_C = np.array([base_length, 0])

# Calculate the coordinates of vertex B using the solved angles
slope_AB = np.tan(np.deg2rad(angle_A_deg))
slope_CB = np.tan(np.deg2rad(180 - angle_C_deg))

# Find the intersection of the two lines to get vertex B
x_B = (-slope_CB * base_length) / (slope_AB - slope_CB)
y_B = slope_AB * x_B
vert_B = np.array([x_B, y_B])

# Create the plot
fig, ax = plt.subplots()

# Plot the triangle sides
vertices_x = [vert_A[0], vert_B[0], vert_C[0], vert_A[0]]
vertices_y = [vert_A[1], vert_B[1], vert_C[1], vert_A[1]]
ax.plot(vertices_x, vertices_y, 'b-', marker='o', markersize=8, label='Triangle ABC')

# Add labels for vertices and angles
ax.text(vert_A[0] - 0.8, vert_A[1], 'A', fontsize=14, va='center')
ax.text(vert_B[0], vert_B[1] + 0.5, 'B', fontsize=14, ha='center')
ax.text(vert_C[0] + 0.8, vert_C[1], 'C', fontsize=14, va='center')

# Angle labels
ax.text(vert_A[0] + 1.2, vert_A[1] + 0.4, f'{angle_A_deg}°', fontsize=12, color='red', weight='bold')
ax.text(vert_B[0] - 1.2, vert_B[1] - 0.6, f'{angle_B_deg}°', fontsize=12, color='red', weight='bold')
ax.text(vert_C[0] - 1.5, vert_C[1] + 0.4, f'{angle_C_deg}°', fontsize=12, color='red', weight='bold')

# Finalize and display the plot as a figure
ax.set_aspect('equal', adjustable='box')
ax.axis('off')  # Turn off the axes to create a figure-like appearance

# Save the plot to a file and show it
plt.savefig('../figs/fig.png')
plt.show()

