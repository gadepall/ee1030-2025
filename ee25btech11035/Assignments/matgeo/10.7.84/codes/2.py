import numpy as np
import matplotlib.pyplot as plt

radius = 3.0
# The length of the tangent from the origin (O) to the point of contact (A)
# was calculated as 9 + 3 * sqrt(10).
oa_length = 9 + 3 * np.sqrt(10)

# The point of contact A is on the line y=x, at a distance of oa_length from the origin.
# x = y, and x^2 + y^2 = oa_length^2  => 2x^2 = oa_length^2 => x = oa_length / sqrt(2)
poc_A = np.array([oa_length / np.sqrt(2), oa_length / np.sqrt(2)])

# The circle's center C is found by moving from A by a distance of the radius
# in a direction perpendicular to the tangent line y=x.
# The normal vector to y=x (direction [1,1]) is [-1,1].
normal_dir = np.array([-1, 1]) / np.sqrt(2)
center_C = poc_A + radius * normal_dir

# Generate data for the tangent lines
x_range = np.linspace(-1, 18, 200)
y_tangent1 = 1 * x_range  # y = x
y_tangent2 = 2 * x_range  # y = 2x

fig, ax = plt.subplots(figsize=(12, 10))

# Plot the circle
circle = plt.Circle(center_C, radius, color='skyblue', fill=False, lw=2, label=f'Circle (radius={radius})')
ax.add_patch(circle)

# Plot the two tangent lines
ax.plot(x_range, y_tangent1, 'g-', label='Tangent y=x')
ax.plot(x_range, y_tangent2, 'orange', linestyle='--', label='Tangent y=2x')

# Plot the key triangle OAC (Origin, Point of Contact, Center)
ax.plot([0, poc_A[0]], [0, poc_A[1]], 'r-', label=f'OA (length={oa_length:.2f})')
ax.plot([poc_A[0], center_C[0]], [poc_A[1], center_C[1]], 'm-', label=f'AC (radius={radius})')
ax.plot([0, center_C[0]], [0, center_C[1]], 'k:', label='Line OC (Angle Bisector)')

# Plot and label the key points
ax.plot(0, 0, 'ko', markersize=8, label='Origin O')
ax.plot(poc_A[0], poc_A[1], 'ro', markersize=8, label='Point of Contact A')
ax.plot(center_C[0], center_C[1], 'bo', markersize=8, label='Center C')

# Add text annotations for clarity
ax.text(poc_A[0] - 1.5, poc_A[1] + 1.5, f'A({poc_A[0]:.1f}, {poc_A[1]:.1f})', color='red')
ax.text(center_C[0] + 0.5, center_C[1], f'C({center_C[0]:.1f}, {center_C[1]:.1f})', color='blue')

ax.set_title('Visualization for Problem 10.7.84', fontsize=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.grid(True, linestyle=':')
ax.legend(loc='upper left')
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-2, 20)
ax.set_ylim(-2, 20)

plt.savefig('2.png')
plt.show()