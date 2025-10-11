import numpy as np
import matplotlib.pyplot as plt

# Define theta
theta = np.linspace(0, 2*np.pi, 400)

# Ellipse parameters
a = 3  # semi-major axis
b = np.sqrt(5)  # semi-minor axis

x = a * np.cos(theta)
y = b * np.sin(theta)

plt.plot(x, y, label=r'$\dfrac{x^2}{9} + \dfrac{y^2}{5} = 1$')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Ellipse Locus")
plt.grid(True)

# Move legend to top-right
plt.legend(loc="upper right")

plt.axis("equal") 
plt.savefig("fig9.png") 
plt.show()