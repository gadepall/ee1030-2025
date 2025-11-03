import matplotlib.pyplot as plt
import numpy as np

# Define slope and intercept
m = 1/2
c = -3/2

# Create x values
x = np.linspace(-2, 10, 400)

# Equation of the line
y = m * x + c

# Plot the line
plt.figure(figsize=(8,6))
plt.plot(x, y, label="y = (1/2)x - 3/2", color="blue")

# Mark the y-intercept point
plt.scatter(0, c, color="blue", marker="o", label="y-intercept (0, -3/2)")

# Draw x and y axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Labels and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of Line: y = (1/2)x - 3/2")
plt.legend()
plt.grid(True)

# Save the graph as PNG
plt.savefig("grapha", dpi=300)

# Show plot
plt.show()
