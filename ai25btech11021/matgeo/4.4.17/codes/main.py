import numpy as np
import matplotlib.pyplot as plt

# Given points A and B
A = np.array([3, -5])
B = np.array([-4, 8])

# Given ratio K
K = 0.5

# Calculate point P dividing AB in ratio K:1
P = (K * B + A) / (K + 1)

# Prepare line segment AB
line_AB_x = [A[0], B[0]]
line_AB_y = [A[1], B[1]]

# Prepare line x + y = 0 (y = -x)
x_vals = np.linspace(-10, 10, 400)
y_vals = -x_vals

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(line_AB_x, line_AB_y, 'b-', label='Line segment AB')
plt.plot(x_vals, y_vals, 'g--', label='Line x + y = 0')

# Plot points
plt.plot(A[0], A[1], 'ro', label='Point A (3, -5)')
plt.plot(B[0], B[1], 'bo', label='Point B (-4, 8)')
plt.plot(P[0], P[1], 'mo', label=f'Point P (divides AB, K={K})')

# Annotate points
plt.text(A[0] + 0.3, A[1], 'A', fontsize=12, color='red')
plt.text(B[0] + 0.3, B[1], 'B', fontsize=12, color='blue')
plt.text(P[0] + 0.3, P[1], 'P', fontsize=12, color='magenta')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of points A, B, P and line x + y = 0')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Save plot
plt.savefig('python_plot.png')
plt.show()
