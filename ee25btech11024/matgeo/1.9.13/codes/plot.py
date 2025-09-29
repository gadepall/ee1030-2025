import numpy as np
import matplotlib.pyplot as plt

A = np.array([-5, 0])
B = np.array([-5, 12])
O = np.array([0, 0])

plt.figure(figsize = (7,7))
plt.plot([O[0], A[0]], [O[1],A[1]], 'g->', label = 'OA = 5 units')
plt.plot([A[0], B[0]], [A[1],B[1]], 'b->', label = 'AB = 12 units')
plt.plot([B[0], O[0]], [B[1],O[1]], 'r->', label = 'OB = 13 units')

plt.scatter(*O, color = "green")
plt.scatter(*A, color = "blue")
plt.scatter(*B, color = "red")

plt.text(O[0]+0.2, O[1]+0.2, "O(0,0)")
plt.text(A[0]+0.2, A[1]+0.2, "A(-5,0)")
plt.text(B[0]+0.2, B[1], "B(-5, 10)")

plt.xlabel("X - AXIS")
plt.ylabel("Y-AXIS")
plt.title("Distance from starting point when man walks from O to A and from A to B")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("fig.png")
plt.show()
