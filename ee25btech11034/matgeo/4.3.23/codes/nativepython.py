import matplotlib.pyplot as plt
import numpy as np

# --- 1. Mathematical Calculation ---

# Define the coordinates of points A and B
A = np.array([3, 2])
B = np.array([5, 1])

# Define the ratio m:n
m = 1
n = 2

# Calculate the coordinates of point P using the section formula
# P = (m*B + n*A) / (m + n)
P = (m * B + n * A) / (m + n)

# The point P lies on the line 3x - 18y + k = 0.
# We can find k by substituting the coordinates of P into the equation:
# 3*P_x - 18*P_y + k = 0  =>  k = 18*P_y - 3*P_x
k = 18 * P[1] - 3 * P[0]

# Print the results of the calculation
print(f"The equation of the line is 3x - 18y + k = 0")
print(f"Calculated value of k: {k:.2f}")


# --- 2. Plotting the Graph ---

# Create a range of x values for plotting the line
x_vals = np.linspace(0, 6, 100)
# Calculate the corresponding y values for the line: 3x - 18y + k = 0
# Rearranged to y = (3x + k) / 18
y_vals = (3 * x_vals + k) / 18

# Create the plot
plt.figure(figsize=(10, 8))

# Plot the line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'm-', label='Line Segment AB')

# Plot the infinite line 3x - 18y + k = 0
plt.plot(x_vals, y_vals, 'c-', label=f'Line 3x - 18y + {k:.0f} = 0')

# Plot the points A, B, and P
plt.plot(A[0], A[1], 'ro', markersize=8)
plt.plot(B[0], B[1], 'bo', markersize=8)
plt.plot(P[0], P[1], 'go', markersize=10) # Make P stand out

# Use annotate to label the points and a legend for the lines
plt.annotate(f'A ({A[0]}, {A[1]})', (A[0] + 0.1, A[1]), fontsize=12, color='red')
plt.annotate(f'B ({B[0]}, {B[1]})', (B[0] + 0.1, B[1]), fontsize=12, color='blue')
plt.annotate(f'P ({P[0]:.2f}, {P[1]:.2f})', (P[0] - 0.7, P[1] - 0.15), fontsize=12, color='green', weight='bold')


# --- 3. Formatting the Plot ---

plt.title('Visualization of Point P on a Line Segment', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)

# Add a legend for the line plots
plt.legend()

# Set the aspect of the plot to be equal
plt.gca().set_aspect('equal', adjustable='box')

# Add a grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Set plot limits to give some space around the points
plt.xlim(2, 6)
plt.ylim(0, 3)

# Show the plot
plt.show()
