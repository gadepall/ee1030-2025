import matplotlib.pyplot as plt
import numpy as np

# Create a range of x values (cost of a pencil)
x = np.linspace(0, 5, 100)

# Calculate the corresponding y values for each equation
# Equation 1: 2x + 3y = 9  => y = (9 - 2x) / 3
y1 = (9 - 2*x) / 3

# Equation 2: 4x + 6y = 18 => y = (18 - 4x) / 6
y2 = (18 - 4*x) / 6

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the first line
plt.plot(x, y1, label='2x + 3y = 9', color='blue', linewidth=4)

# Plot the second line on top of the first one with a different style to show they are identical
plt.plot(x, y2, label='4x + 6y = 18', color='red', linestyle='--', linewidth=2)

# Add titles and labels
plt.title("Both Equations Represent the Same Line")
plt.xlabel("Cost of Pencil (x)")
plt.ylabel("Cost of Eraser (y)")
plt.grid(True)
plt.legend()
plt.tight_layout()


# Save the plot to a file
plt.savefig("Figure_2.png")

