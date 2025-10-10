
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA


A = np.array([1,5]).reshape(-1,1)
B = np.array([4,6]).reshape(-1,1)
e_2 = np.array([0,1]).reshape(-1,1)
M = np.array([2.5,5.5]).reshape(-1,1)

y = (LA.norm(A)*LA.norm(A) - LA.norm(B)*LA.norm(B))/(2*(A-B).T@e_2)


y = y.item()

P = np.array([0,y]).reshape(-1,1)

plt.plot([A[0,0],B[0,0]],[A[1,0],B[1,0]], 'orange', label = "Line Segment $AB$")
plt.plot([P[0,0],M[0,0]],[P[1,0],M[1,0]], 'b--', label = "Perpendicular Bisector")


tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points", 
                 xytext=(20,5), 
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

