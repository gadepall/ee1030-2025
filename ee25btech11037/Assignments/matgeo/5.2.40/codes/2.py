import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define hard-coded values ---

# Coefficients of the equations for plotting the curves
# 4/x + 3y = 14
# 3/x - 4y = 23
a1, b1, c1 = 4.0, 3.0, 14.0
a2, b2, c2 = 3.0, -4.0, 23.0

# Hard-coded solution for the intersection point P
x_point = 0.2  # This is 1/5
y_point = -2.0

# --- 2. Prepare data and create the plot ---

# Prepare data for plotting the curves
x_vals = np.linspace(-2, 2, 800)
x_vals[x_vals == 0] = 1e-9  # Avoid division by zero

# Rearrange equations to solve for y
y1_vals = (c1 - a1 / x_vals) / b1
y2_vals = (c2 - a2 / x_vals) / b2

# Create the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the two functions
ax.plot(x_vals, y1_vals, label=f'${int(a1)}/x + {int(b1)}y = {int(c1)}$')
ax.plot(x_vals, y2_vals, label=f'${int(a2)}/x {int(b2)}y = {int(c2)}$')

# Plot the intersection point using the hard-coded values
ax.plot(x_point, y_point, 'ro', markersize=10, label='Intersection Point P')

# Format and add the coordinate text
coord_text = f'P ({x_point:.2f}, {y_point:.2f})'
ax.text(x_point + 0.05, y_point, coord_text, fontsize=12, color='red', va='center')

# --- 3. Formatting and Output ---

# Add titles, labels, and grid
ax.set_title('Plot of Equations with Hard-coded Intersection', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_ylim(-10, 10)
ax.set_xlim(-2, 2)
ax.legend(fontsize=12)
ax.grid(True)

# Save the figure to '1.png'
plt.savefig('2.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
