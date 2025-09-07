import numpy as np
import matplotlib.pyplot as plt
#local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen


# Given points
A = np.array(([2,-5])).reshape(-1,1)
B = np.array(([5,2])).reshape(-1,1)

# Ratio m:n = 2:3
m, n = 2, 3

# Point dividing AB in ratio m:n
P = (n*A + m*B) / (m+n)

# Generating line AB
def line_gen(A,B):

    len = 100
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    
    
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB

x_AB = line_gen(A,B)

# Plotting line AB
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')

# Plotting points A, B, P
tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']

for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.1f}, {tri_coords[1,i]:.1f})',
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points",
                 xytext=(20,-10), ha='center')

# Axis styling
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()



