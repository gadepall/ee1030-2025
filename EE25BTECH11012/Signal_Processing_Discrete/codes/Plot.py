import numpy as np
import matplotlib.pyplot as plt

# Define the range for x (avoiding 0 to prevent division by zero)
x = np.linspace(-2, 2, 400)
x = x[x != 0] 

# Define the functions
coth_x = 1 / np.tanh(x)
approx_x = 1 / x

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, coth_x, label=r'$\coth(x)$', color='blue', linewidth=2)
plt.plot(x, approx_x, '--', label=r'Approximation $\frac{1}{x}$', color='red', linewidth=2)

# Set limits and labels
plt.ylim(-10, 10)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title(r'Comparison of $\coth(x)$ and its Approximation $\frac{1}{x}$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Highlight the region |x| < 1
plt.fill_between(x, -10, 10, where=(np.abs(x) < 1), color='green', alpha=0.1, label='Region $|x| < 1$')

plt.show()