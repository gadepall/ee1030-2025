import numpy as np
import matplotlib.pyplot as plt

A = np.array([-5, 4])
B = np.array([-1, 6])

a = B[0] - A[0]
b = B[1] - A[1]
c = (np.dot(B, B) - np.dot(A, A)) / 2

x = np.linspace(-10, 5, 400)
y = (c - a * x) / b

plt.scatter(*A, color='red', label='A(-5,4)')
plt.scatter(*B, color='green', label='B(-1,6)')
plt.plot(x, y, color='blue', label='Equidistant line')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Equidistant Points: Line and Given Points')
plt.grid(True)
plt.tight_layout()
plt.axis('square')

plt.xlim(-10, 20)
plt.ylim(-10, 20)

plt.savefig('equidistant_plot.png')
plt.show()
