import numpy as np
import matplotlib.pyplot as plt

# --- Hardcoded values for the coefficients and the solution ---
a1, b1, c1 = 3.0, 2.0, 12.0 # For 3/x + 2/y = 12
a2, b2, c2 = 2.0, 3.0, 13.0 # For 2/x + 3/y = 13

# Hardcoded solution for the system
x_point = 0.5
y_point = 1.0 / 3.0

# --- Prepare data for plotting ---
# We need to handle vertical asymptotes and x=0
x_vals = np.linspace(-1, 2, 800)
x_vals[x_vals == 0] = 1e-9 # Avoid division by zero for 1/x

# Rearrange equations to solve for y:
# Eq1: 2/y = 12 - 3/x  =>  y = 2 / (12 - 3/x)
# Eq2: 3/y = 13 - 2/x  =>  y = 3 / (13 - 2/x)
with np.errstate(divide='ignore', invalid='ignore'):
    y1_vals = b1 / (c1 - a1 / x_vals)
    y2_vals = b2 / (c2 - a2 / x_vals)

# --- Create the plot ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the two functions
ax.plot(x_vals, y1_vals, label=f'${int(a1)}/x + {int(b1)}/y = {int(c1)}$')
ax.plot(x_vals, y2_vals, label=f'${int(a2)}/x + {int(b2)}/y = {int(c2)}$')

# Plot the intersection point
ax.plot(x_point, y_point, 'ro', markersize=10, label='Intersection Point P')

# Format and add the coordinate text
coord_text = f'P ({x_point:.2f}, {y_point:.2f})'
ax.text(x_point + 0.05, y_point, coord_text, fontsize=12, color='red', va='center')

# Formatting
ax.set_title('Solving System of Equations (Hardcoded Solution)', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
# Adjust plot limits to get a good view of the intersection
ax.set_ylim(-2, 2)
ax.set_xlim(-1, 2)
ax.legend(fontsize=12)
ax.grid(True)

# Save the figure
plt.savefig('2.png')

# Display the plot
plt.show()