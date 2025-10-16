import numpy as np
import matplotlib.pyplot as plt
from libs.funcs import line_norm # Import the required function

# The value of 'a' we calculated
a = 5/3

# This is in the form n.T @ x + k = 0
# The normal vector n is [5, -9]
# The constant term is 21, so n.T @ x = -21

# 1. Define the line's properties for the plotting function
n = np.array([5, -9]).reshape(-1, 1)
c = -21

# 2. Generate the coordinate data for the line
# We use a large range (-10, 10) to ensure the line is long enough for the plot
line_coords = line_norm(n, c, -10, 10)

# 3. Define the point that lies on the line
P = np.array([3, 4])

# 4. Plot the results
plt.plot(line_coords[0, :], line_coords[1, :], label=f'Line 3y = ({a:.2f})x + 7')
plt.plot(P[0], P[1], 'ro', label='Point (3, 4)') # 'ro' for red circle

# Add labels and a grid for better visualization
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Verification Plot")
plt.grid(True)
plt.legend()
plt.axis('equal') # Ensures correct aspect ratio

# Display the plot
plt.show()
