import matplotlib.pyplot as plt
import numpy as np
# Part 1: Define points for each k and plot points
k_values = [0.5, 2]  # values of k for collinearity
plt.figure(figsize=(8,6))
for k in k_values:
    A = np.array([k+1, 2*k])
    B = np.array([3*k, 2*k+3])
    C = np.array([5*k-1, 5*k])
     plt.scatter(*A, color='red')
    plt.scatter(*B, color='green')
    plt.scatter(*C, color='blue')
     plt.text(A[0], A[1], 'A', fontsize=12, color='red', ha='right')
    plt.text(B[0], B[1], 'B', fontsize=12, color='green', ha='right')
    plt.text(C[0], C[1], 'C', fontsize=12, color='blue', ha='right')
      x_line = np.linspace(min(A[0], B[0], C[0])-1, max(A[0], B[0], C[0])+1, 100)
    y_line = ((B[1]-A[1])/(B[0]-A[0])) * (x_line - A[0]) + A[1]
    plt.plot(x_line, y_line, label=f'Line through A and B for k={k}')

plt.title('Collinearity of Points A, B, C for values of k')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
