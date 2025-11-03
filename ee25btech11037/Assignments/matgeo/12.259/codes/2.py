import matplotlib.pyplot as plt

# --- 1. Define the initial guess and system of equations ---

# The starting point for the iteration
start_point = (1.0, 1.0, 1.0)
x = list(start_point) # Use a mutable list for calculations


print(f"Initial point: ({x[0]}, {x[1]}, {x[2]})")



# Calculate the new x[0] using the initial values of x[1] and x[2]
x[0] = (13 - 2*x[1] - 1*x[2]) / 5.0
print(f"Step 1 -> New x[0] = {x[0]:.4f}. Current point: ({x[0]:.4f}, {x[1]:.4f}, {x[2]:.4f})")

# Calculate the new x[1] using the NEW x[0] and the initial x[2]
x[1] = (-22 - (-2*x[0]) - 2*x[2]) / 5.0
print(f"Step 2 -> New x[1] = {x[1]:.4f}. Current point: ({x[0]:.4f}, {x[1]:.4f}, {x[2]:.4f})")

# Calculate the new x[2] using the NEW x[0] and NEW x[1]
x[2] = (14 - (-1*x[0]) - 2*x[1]) / 8.0
print(f"Step 3 -> New x[2] = {x[2]:.4f}. Current point: ({x[0]:.4f}, {x[1]:.4f}, {x[2]:.4f})")

final_point = tuple(x)
print(f"Final point after one iteration: ({final_point[0]:.4f}, {final_point[1]:.4f}, {final_point[2]:.4f})")

# --- Plot the results in 3D ---
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the starting point
ax.scatter(start_point[0], start_point[1], start_point[2], c='blue', s=100, label='Start Point', depthshade=True)
ax.text(start_point[0], start_point[1], start_point[2], f'  ({start_point[0]:.1f}, {start_point[1]:.1f}, {start_point[2]:.1f})', color='blue', fontsize=12)

# Plot the calculated point after one iteration
ax.scatter(final_point[0], final_point[1], final_point[2], c='red', s=100, label='Point after 1 Iteration', depthshade=True)
ax.text(final_point[0], final_point[1], final_point[2], f'  ({final_point[0]:.2f}, {final_point[1]:.2f}, {final_point[2]:.2f})', color='red', fontsize=12)

# Setting labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Plot of Start Point vs. Single Iteration Result')
ax.legend()
ax.grid(True)

# Improve layout
plt.tight_layout()
plt.savefig('2.png')
plt.show()

