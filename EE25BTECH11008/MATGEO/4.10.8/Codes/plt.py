import numpy as np
import matplotlib.pyplot as plt

m1, c1 = 1.5, 2 
m2, c2 = -0.5, 5     
A = np.array([0, c1])
B = np.array([0, c2])
x_intersect = (c2 - c1) / (m1 - m2)
y_intersect = m1 * x_intersect + c1
C = np.array([x_intersect, y_intersect])
triangle = np.array([A, B, C, A]) 

plt.figure(figsize=(6,6))
plt.plot(triangle[:,0], triangle[:,1], 'b-o', label='Triangle')
plt.axvline(0, color='k', linewidth=0.8) 
plt.axhline(0, color='k', linewidth=0.8) 
x_vals = np.linspace(min(0, C[0])-1, max(C[0]+1, 2), 100)
plt.plot(x_vals, m1*x_vals + c1, 'r--', label=f'y={m1}x+{c1}')
plt.plot(x_vals, m2*x_vals + c2, 'g--', label=f'y={m2}x+{c2}')

plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='black')
plt.text(A[0]-0.3, A[1]+0.1, 'A')
plt.text(B[0]-0.3, B[1]+0.1, 'B')
plt.text(C[0]+0.1, C[1]+0.1, 'C')
plt.grid(True)
plt.axis('equal')
plt.title('Triangle formed by lines and x=0')
plt.show()
