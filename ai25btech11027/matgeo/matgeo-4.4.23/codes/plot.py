import numpy as np
import matplotlib.pyplot as plt

# Define the range for x
x = np.linspace(-5, 10, 400)

# Equation 1: x - 2y + 3 = 0  =>  y = (x + 3)/2
y1 = (x + 3) / 2

# Equation 2: 2x - 4y = 5  =>  y = (2x - 5)/4
y2 = (2*x - 5) / 4

plt.figure(figsize=(8,6))
plt.plot(x, y1, label=r'$x - 2y + 3 = 0$', color='blue')
plt.plot(x, y2, label=r'$2x - 4y = 5$', color='red')

plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis

plt.legend()
plt.title('Plot of the Lines')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

