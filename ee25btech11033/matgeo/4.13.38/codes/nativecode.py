import matplotlib.pyplot as plt
import numpy as np

# --- Define the points ---
P = (2, 2)
Q = (6, -1)
R = (7, 3)
point_parallel = (1, -1)

# --- Calculations ---
# 1. Calculate the midpoint S of QR
S = ((Q[0] + R[0]) / 2, (Q[1] + R[1]) / 2)

# 2. Define the triangle vertices for plotting
triangle = [P, Q, R, P]  # Close the triangle by returning to P
triangle_x, triangle_y = zip(*triangle)

# 3. Define the median line PS
median_ps_x = [P[0], S[0]]
median_ps_y = [P[1], S[1]]

# 4. Define the parallel line
# Equation: 2x + 9y + 7 = 0  =>  y = (-2x - 7) / 9
# Generate a range of x-values for the line
x_vals = np.linspace(-2, 10, 100)
y_vals = (-2 * x_vals - 7) / 9

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the triangle
ax.plot(triangle_x, triangle_y, 'b-', label='Triangle PQR', linewidth=2)

# Plot the median PS
ax.plot(median_ps_x, median_ps_y, 'g--', label='Median PS', linewidth=2)

# Plot the parallel line
ax.plot(x_vals, y_vals, 'r-', label='Parallel Line (2x + 9y + 7 = 0)', linewidth=2)

# Plot and label the points
points = {'P(2,2)': P, 'Q(6,-1)': Q, 'R(7,3)': R, 'S(6.5,1)': S, '(1,-1)': point_parallel}
for label, (x, y) in points.items():
    ax.plot(x, y, 'ko', markersize=8)
    ax.text(x + 0.2, y + 0.2, label, fontsize=12)

# --- Formatting the plot ---
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.legend(fontsize=12)
ax.grid(True)
ax.set_aspect('equal', adjustable='box') # Ensure the scale is equal for a proper geometric representation

# Set plot limits for better visibility
plt.xlim(-1, 10)
plt.ylim(-3, 5)
# Save the plot
plt.savefig('../figs/fig.png')
# Show the plot
plt.show()

