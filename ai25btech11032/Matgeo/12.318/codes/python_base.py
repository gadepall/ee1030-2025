import numpy as np
import matplotlib.pyplot as plt

# Define the base factor polynomial
def f(x):
    return (x-1.0)*(x-0.5)*(x-5.0)*(x-7.0)*(x-3.0)*(x-4.0)

# Range of x values
xs = np.linspace(-1, 8, 600)
ys = f(xs)

# The six fixed roots
roots = np.array([1.0, 0.5, 5.0, 7.0, 3.0, 4.0])

# Plot the curve
plt.plot(xs, ys, label="f(x) = (x-1)(x-0.5)(x-5)(x-7)(x-3)(x-4)")

# Mark the roots on the x-axis
plt.scatter(roots, np.zeros_like(roots), color="red", zorder=5, label="Fixed roots")

# Draw x-axis
plt.axhline(0, color="black", linewidth=0.8)

# Labels and title
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Base Factor Polynomial with Fixed Roots")
plt.legend()
plt.savefig("new_poly_dim.png")
plt.show()

