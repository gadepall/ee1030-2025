import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the curve
def curve_y(x):
    return 1 + np.abs(x + 1)

# Define the integration function for the area
def integrand(x):
    return curve_y(x)

# Define the limits of integration
x_lower = -3
x_upper = 3

# Calculate the area using numerical integration
area, _ = quad(integrand, x_lower, x_upper)
print(f"The area of the region bounded by the curves is: {area:.2f} square units")

# Generate x values for plotting
x_vals = np.linspace(x_lower, x_upper, 400)
y_vals = curve_y(x_vals)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the curve y = 1 + |x + 1|
plt.plot(x_vals, y_vals, label=r'$y = 1 + |x + 1|$', color='blue')

# Plot the lines x = -3 and x = 3
plt.axvline(x=x_lower, color='red', linestyle='--', label=r'$x = -3$')
plt.axvline(x=x_upper, color='red', linestyle='--', label=r'$x = 3$')

# Plot the line y = 0 (x-axis)
plt.axhline(y=0, color='red', linestyle='--', label=r'$y = 0$')

# Fill the area under the curve
x_fill = np.linspace(x_lower, x_upper, 400)
y_fill = curve_y(x_fill)
plt.fill_between(x_fill, y_fill, where=(y_fill > 0), color='lightblue', alpha=0.5, label='Bounded Area')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Region Bounded by $y = 1 + |x + 1|$, $x = -3$, $x = 3$, $y = 0$')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(bottom=0) # Ensure y-axis starts from 0 for clarity of area
plt.show()
