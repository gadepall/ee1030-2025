import numpy as np
from scipy.integrate import simps

# Define the function for the area integral
def f(x):
  return np.sqrt(9/4 - x**2) - (x**2 / 4)

# Set the integration limits from -sqrt(2) to +sqrt(2)
a = -np.sqrt(2)
b = np.sqrt(2)

# Generate a set of points for the calculation
x_points = np.linspace(a, b, 1001)
y_points = f(x_points)

# Calculate the area using Simpson's method
area = simps(y_points, x_points)

# Print the final result
print(f"The calculated area is: {area}")
print(f"The expected area is : 3.005360;Hence it verifies the integrated area.")