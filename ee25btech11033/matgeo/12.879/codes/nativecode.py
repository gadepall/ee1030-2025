import numpy as np
import matplotlib.pyplot as plt

# Define the vectors from the problem statement
a = np.array([1, 1])
b = np.array([0, 3 * np.sqrt(2)])

# Step 1: Solve for the value of x
# According to the least squares method, x = (a^T * b) / (a^T * a)
# This is equivalent to the dot product a.b / a.a
a_dot_b = np.dot(a, b)
a_dot_a = np.dot(a, a)

x_opt = a_dot_b / a_dot_a

# Step 2: Calculate the residual vector and its norm
# The residual vector r = ax - b
residual_vector = (x_opt * a) - b

# The norm of the residual vector is ||ax - b||
norm_value = np.linalg.norm(residual_vector)

print(f"The norm of the vector (ax - b) is: {norm_value}")

# Step 3: Plot the solution and display the norm
# Calculate the projection of b onto a (the vector ax)
proj_b_on_a = x_opt * a

# Create the plot
plt.figure(figsize=(9, 9))

# Plot the line for vector a (the subspace)
line_end = 2 * a
plt.plot([-a[0], line_end[0]], [-a[1], line_end[1]], 'r-', label='Line defined by vector a (subspace)')

# Plot vector b
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector b')

# Plot the projection vector (ax)
plt.quiver(0, 0, proj_b_on_a[0], proj_b_on_a[1], angles='xy', scale_units='xy', scale=1, color='g', label='Projection of b onto a (ax)')

# Plot the residual vector (r = ax - b)
# Note: the residual r is actually ax - b, so we plot from b to ax
plt.quiver(b[0], b[1], proj_b_on_a[0] - b[0], proj_b_on_a[1] - b[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Residual vector r = ax - b')

# Add text annotation for the norm
mid_point_residual = (proj_b_on_a + b) / 2
plt.text(mid_point_residual[0] + 0.1, mid_point_residual[1], f'||ax - b|| = {norm_value:.4f}', fontsize=12, color='purple')


# Mark the points
plt.plot(b[0], b[1], 'bo')
plt.plot(proj_b_on_a[0], proj_b_on_a[1], 'go')
plt.plot(0, 0, 'ko') # Origin

# Add text labels for points
plt.text(b[0] + 0.1, b[1], f'b ({b[0]:.2f}, {b[1]:.2f})')
plt.text(proj_b_on_a[0] + 0.1, proj_b_on_a[1], f'ax ({proj_b_on_a[0]:.2f}, {proj_b_on_a[1]:.2f})')
plt.text(0.1, 0.1, 'Origin (0,0)')

# Set plot limits and labels
max_val = 5
plt.xlim(-max_val, max_val)
plt.ylim(-2, max_val)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

# Save the plot
plt.savefig('../figs/fig.png')
plt.show()
