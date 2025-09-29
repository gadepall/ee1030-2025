import matplotlib.pyplot as plt

# Points
A = (2, 1)
B = (5, -1)
C = (-1, 3)

# Plot points
plt.scatter(*A, color='red', label='A(2,1)')
plt.scatter(*B, color='blue', label='B(5,-1)')
plt.scatter(*C, color='green', label='C(-1,3)')

# Plot line through A and C
x_values = [A[0], C[0]]
y_values = [A[1], C[1]]
plt.plot(x_values, y_values, 'k--', label='Line through A and C')

plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Collinear Points for p=5')

# Save the plot as an image file
plt.savefig('python_plot.png')  # Saves to current directory

plt.show()
