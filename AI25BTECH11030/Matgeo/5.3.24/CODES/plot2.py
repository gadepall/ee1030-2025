import numpy as np
import matplotlib.pyplot as plt

# Coefficient matrix and RHS from the image
A = np.array([
    [3, -5],
    [9, -2]
])
b = np.array([4, 7])

# Solve for vector x
x = np.linalg.solve(A, b)

# Print solution in matrix form
print("Solution vector x:")
print(np.array([[x[0]], [x[1]]]))

# Plot both lines
fig, ax = plt.subplots()

# Line L: 3x - 5y = 4 => y = (3x - 4)/5
x_vals = np.linspace(-2, 6, 100)
y_L = (3*x_vals - 4)/5
ax.plot(x_vals, y_L, label='3x - 5y = 4 (L)')

# Line K: 9x - 2y = 7 => y = (9*x_vals - 7)/2
y_K = (9*x_vals - 7)/2
ax.plot(x_vals, y_K, label='9x - 2y = 7 (K)')

# Mark intersection point
ax.plot(x[0], x[1], 'ro', label='Intersection')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
ax.set_title('Graph of the two lines')

plt.savefig('fig1.png')
plt.show()

