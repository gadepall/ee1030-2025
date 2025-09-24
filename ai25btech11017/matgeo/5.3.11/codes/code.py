import numpy as np
import matplotlib.pyplot as plt

# Define x values
x = np.linspace(-10, 10, 400)

# First equation: 5x - 3y = 11  -> y = (5x - 11)/3
y1 = (5*x - 11)/3

# Second equation: -10x + 6y = 22 -> y = (10x + 22)/6
y2 = (10*x + 22)/6

# Plot the lines
plt.plot(x, y1, label="5x - 3y = 11")
plt.plot(x, y2, label="-10x + 6y = 22")

# Labels and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of Linear Equations")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)

# Show legend
plt.legend()

# Save the figure
plt.savefig("lines.png", dpi=300)

# Show the plot
plt.show()
