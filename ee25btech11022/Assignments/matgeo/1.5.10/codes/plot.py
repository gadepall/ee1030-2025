import matplotlib.pyplot as plt
import numpy as np
from call import get_points

P, k, A, B = get_points()

plt.figure(figsize=(7,5))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='Segment AB')
plt.scatter(A[0], A[1], color='red', label='A(1, -5)')
plt.scatter(B[0], B[1], color='green', label='B(-4, 5)')
plt.scatter(P[0], P[1], color='orange', s=100, label=f'Dividing Point ({P[0]:.2f}, {P[1]:.2f})')
plt.axhline(0, color='gray', ls='--', label='x-axis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Division of segment AB by X-axis')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

