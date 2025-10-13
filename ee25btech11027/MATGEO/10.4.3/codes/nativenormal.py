import numpy as np
import matplotlib.pyplot as plt

contact_x = 2
contact_y = contact_x + 1/contact_x

print(f"--- Native Python Solution ---")
print(f"The point of contact is ({contact_x}, {contact_y})")

# --- 2. Plotting ---
# Generate x values for plotting
x_vals = np.linspace(0.1, 5, 400)

# Define the functions for the plot
curve = x_vals + 1/x_vals
line = (3*x_vals - 7) / 4
normal_line = (-4/3)*(x_vals - contact_x) + contact_y

# Create the plot
plt.figure(figsize=(10, 8))
plt.plot(x_vals, curve, label='Curve: $y = x + 1/x$', color='blue')
plt.plot(x_vals, line, label='Line: $3x - 4y - 7 = 0$', color='red', linestyle='--')
plt.plot(x_vals, normal_line, label='Normal to Curve', color='green')

# Plot the point of contact
plt.scatter(contact_x, contact_y, color='black', zorder=5)
plt.text(contact_x + 0.1, contact_y + 0.1, f'P({contact_x}, {contact_y:.1f})', fontsize=12)

# Formatting
plt.title('Geometric Solution')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal') # Ensures perpendicular lines look perpendicular
plt.ylim(-1, 6)
plt.xlim(-1, 6)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/10.4.3/figs/figure1.png")
plt.show()
