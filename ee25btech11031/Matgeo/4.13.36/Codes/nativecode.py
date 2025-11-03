import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

P = np.array([2, 1])

#solving Ax=b, to find x
A = np.array([[3, -1],
              [2,  1]])
b = np.array([5, 3])
R = LA.solve(A, b)

A = np.array([[1, 3],
              [2, 1]])
b = np.array([5, 3])
Q = LA.solve(A, b)

plt.scatter([P[0],Q[0],R[0]], [P[1],Q[1],R[1]])

plt.plot([P[0],R[0]],[P[1],R[1]], label = "PR: 3x-y=5")
plt.plot([P[0],Q[0]],[P[1],Q[1]], label = "PQ: x+3y=5")
plt.plot([0,2], [3,-1], c='green', label = "QR: $2x+y=3$")

R_p = np.array([R[0],R[1]], dtype=np.float64).reshape(-1,1)
Q_p = np.array([Q[0],Q[1]], dtype=np.float64).reshape(-1,1)
P_p = np.array([2,1]).reshape(-1,1)


tri_coords = np.block([[P_p,Q_p,R_p]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n',
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points", 
                 xytext=(0.2,0.2), 
                 ha='center') 


ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig("../Figs/plot(py).png")
plt.show()



