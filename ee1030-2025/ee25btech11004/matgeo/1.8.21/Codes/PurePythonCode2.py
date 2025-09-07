import sys 
import ctypes

import numpy as np
import matplotlib.pyplot as plt


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


v1 = np.array([7,6]).reshape(-1,1)
v2 = np.array([3,4]).reshape(-1,1)

e1 = np.array([1,0]).reshape(-1,1)

diff = (v1-v2).T

dot_product = diff@e1



denominator = 2*(dot_product)

norm1 = np.linalg.norm(v1)
norm1 = norm1*norm1

norm2 = np.linalg.norm(v2)
norm2 = norm2*norm2


xcoord = (norm1-norm2)/(denominator)
print(xcoord)

x = xcoord[0,0]


reqdpoint = np.array([x,0]).reshape(-1,1)



allcoords = np.block([v1,v2,reqdpoint])




x_1r = line_gen(v1,reqdpoint)
x_2r = line_gen(v2,reqdpoint)

#Plotting all lines
plt.plot(x_1r[0,:],x_1r[1,:],label='$AB$')
plt.plot(x_2r[0,:],x_2r[1,:],label='$BC$')



#Labeling the coordinates
colors = np.arange(1,4)
allcoords = np.block([[v1,v2,reqdpoint]])
plt.scatter(allcoords[0,:], allcoords[1,:], c=colors)
vert_labels = ['v1','v2','required point']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({allcoords[0,i]:.2f}, {allcoords[1,i]:.2f})',
                 (allcoords[0,i], allcoords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(25,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.grid() # minor
plt.axis('equal')


plt.show()