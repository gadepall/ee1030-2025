import numpy as np
import matplotlib.pyplot as plt

# Set the values of a and b
a = 5
b = 1

# Define the equations
def line_eq1(x):
    return (7 - 2*x) / 3  # y = (7 - 2x) / 3

def line_eq2(x, a, b):
    return (3*a + b - 2 - (a - b)*x) / (a + b)  # y = (3a + b - 2 - (a - b)x) / (a + b)

# Generate x values
x_vals = np.linspace(-10, 10, 400)

# Calculate the corresponding y values for both lines
y_vals_eq1 = line_eq1(x_vals)
y_vals_eq2 = line_eq2(x_vals, a, b)

# Plot the lines
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals_eq1, label="2x + 3y = 7", color="blue")
plt.plot(x_vals, y_vals_eq2, label=f"({a} - {b})x + ({a} + {b})y = {3*a + b - 2}", color="red", linestyle="--")

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the Linear Equations')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

