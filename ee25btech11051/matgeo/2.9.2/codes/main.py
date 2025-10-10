import matplotlib.pyplot as plt
import numpy as np
import ctypes
import os
import sys


A=np.array([-5, 3], dtype=np.float64)
B=np.array([5, 3], dtype=np.float64)
m=len(A)

D=B-A

fig, ax=plt.subplots()

norm = np.linalg.norm(D)

t=(1.7/2)*norm

C1=np.array([0, 3+t], dtype=np.float64)
C2=np.array([0, 3-t], dtype=np.float64)

def line_gen_num(A,B,num):
  dim = A.shape[0]
  x_AB = np.zeros((dim,num))
  lam_1 = np.linspace(0,1,num)
  for i in range(num):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_AB = line_gen_num(A, B, 20)
x_BC1 = line_gen_num(C1, B, 20)
x_BC2 = line_gen_num(C2, B, 20)
x_AC1 = line_gen_num(A, C1, 20)
x_AC2 = line_gen_num(A, C2, 20)

plt.grid()
plt.title('2.9.2')
plt.plot(x_AB[0, :], x_AB[1, :], 'r--', label='Line from A to B')
plt.plot(x_BC1[0, :], x_BC1[1, :], 'r--') 
plt.plot(x_BC2[0, :], x_BC2[1, :], 'r--') 
plt.plot(x_AC1[0, :], x_AC1[1, :], 'r--') 
plt.plot(x_AC2[0, :], x_AC2[1, :], 'r--') 

plt.plot(A[0], A[1], 'go', label='Point A')  
plt.annotate('(-5,3)', xy=(A[0],A[1]), fontsize=12)
plt.plot(B[0], B[1], 'go', label='Point B')  
plt.annotate('(5,3)', xy=(B[0],B[1]), fontsize=12)
plt.plot(C1[0], C1[1], 'bo', label='Point C1')  
plt.annotate('(0,11.5)', xy=(C1[0],C1[1]), fontsize=12)
plt.plot(C2[0], C2[1], 'bo', label='Point C2')  
plt.annotate('(0,-5.5)', xy=(C2[0],C2[1]), fontsize=12)

for axis in ['bottom', 'left']:
    ax.spines[axis].set_color('black')
    ax.spines[axis].set_linewidth(2)

plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.savefig('/home/shreyas/GVV_Assignments/matgeo/2.9.2/figs/fig1.png')

plt.show()
