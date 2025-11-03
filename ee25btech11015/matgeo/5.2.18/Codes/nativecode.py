import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(-5, 5, 400)

# Define the two lines
y1 = (9 - 8*x)/5   # from 8x + 5y = 9
y2 = (4 - 3*x)/2   # from 3x + 2y = 4

# Plot the lines
plt.plot(x, y1, label=r'$8x + 5y = 9$', color='b')
plt.plot(x, y2, label=r'$3x + 2y = 4$', color='g')

# Intersection point (-1, 5)
plt.plot(-1, 5, 'ro')  
plt.text(-1.2, 5.2, '(-1, 5)', color='r')

# Labels and grid
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution of the System using Graph")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Show plot
plt.show()
