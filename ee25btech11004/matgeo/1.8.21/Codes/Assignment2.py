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


c_lib=ctypes.CDLL('./main.so')

# Define the argument types for the x function
c_lib.xfinder.argtypes = [ctypes.c_float, ctypes.c_float,ctypes.c_float, ctypes.c_float]
# Define the return type of the x function
c_lib.xfinder.restype = ctypes.c_float
# --- Define Points and Calculate 'm' using C function ---

v1 = np.array([7,6])
v2 = np.array([3,4])

xcoord = c_lib.xfinder(
    ctypes.c_float(v1[0]),
    ctypes.c_float(v1[1]), 
    ctypes.c_float(v2[0]), 
    ctypes.c_float(v2[1])
)

v1 = np.array([7,6]).reshape(-1,1)
v2 = np.array([3,4]).reshape(-1,1)

reqdpoint = np.array([xcoord, 0]).reshape(-1,1)

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