#Code by GVV Sharma
#July 22, 2024
#released under GNU GPL
#Line 


import sys                                        
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

def line_norm(n,c,k1,k2):
    e1 = np.array(([1,0])).reshape(-1,1)
    e2 = np.array(([0,1])).reshape(-1,1)
    omat = np.array(([0,1],[-1,0]))
    c = c/LA.norm(n)
    n = n/LA.norm(n)
    if c==0:
        A = np.zeros((2,1))
    elif np.array_equal(n, e1):
        A = np.array(([c, 0])).reshape(-1,1) 
    elif np.array_equal(n, e2):
        A = np.array(([0, c])).reshape(-1,1) 
    else:
        A = np.array(([c/n[0][0], 0])).reshape(-1,1) 
    m = omat@n
    return line_dir_pt(m,A,k1,k2)

def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
  
#Line parameters
n1 = np.array(([1,0])).reshape(-1,1)
c1 = -2
n2 = np.array(([1, -7])).reshape(-1,1) 
c2 = -2
n3 = np.array(([2, -3])).reshape(-1,1) 
c3 =  -4
n4 = np.array(([0, -1])).reshape(-1,1) 
c4 = 0

k1 = -5
k2 = 3
#Generating Lines
x_A = line_norm(n1,c1,k1,k2)
x_B = line_norm(n2,c2,k1,k2)
x_C = line_norm(n3,c3,k1,k2)
x_D = line_norm(n4,c4,k1,k2)

#Plotting all lines
plt.plot(x_A[0,:],x_A[1,:],label='$1$')
plt.plot(x_B[0,:],x_B[1,:],label='$2$')
plt.plot(x_C[0,:],x_C[1,:],label='$3$')
plt.plot(x_D[0,:],x_D[1,:],label='$4$')



# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend()
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/fig.png')
