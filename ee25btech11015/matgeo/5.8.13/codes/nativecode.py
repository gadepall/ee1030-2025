import numpy as np
import matplotlib.pyplot as plt

# Define range for x
x = np.linspace(0, 50, 400)

# Equations:
# 1) x - y = 26  --> y = x - 26
# 2) x - 3y = 0  --> y = x / 3
y1 = x - 26
y2 = x / 3

# Plot the lines
plt.plot(x, y1, label=r'$x - y = 26$')
plt.plot(x, y2, label=r'$x - 3y = 0$')

# Plot the intersection point
plt.plot(39, 13, 'ro', label='Solution (39, 13)')

# Labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphical solution of the system')
plt.grid(True)
plt.legend()
plt.xlim(0, 50)
plt.ylim(0, 50)

plt.show()
