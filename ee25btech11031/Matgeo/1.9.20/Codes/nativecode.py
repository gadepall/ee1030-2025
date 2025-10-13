import sys
sys.path.insert(0, '/home/sai-sreevallabh/Matrix_Theory/Matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

#local imports
from line.funcs import *



A = np.array([5,-2]).reshape(-1,1)
B = np.array([-3,2]).reshape(-1,1)
e_2 = np.array([0,1]).reshape(-1,1)

y = (LA.norm(A)*LA.norm(A) - LA.norm(B)*LA.norm(B))/(2*(A-B).T@e_2)

y = y.item()

P = np.array([0,y]).reshape(-1,1)

x_AP = line_gen(A,P)
x_PB = line_gen(P,B)


plt.plot(x_AP[0,:],x_AP[1,:],label='Line Segment $PA$')
plt.plot(x_PB[0,:],x_PB[1,:],label='Line Segment $PB$')

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
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.savefig("../Figs/plot(py).png")
plt.show()





