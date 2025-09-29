import math
import sys 
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

from line.funcs import *

#if using termux
#import subprocess
#import shlex

X = np.array([6,-6] , dtype = np.float64).reshape(-1,1)
Y = np.array([-4,-1] , dtype = np.float64).reshape(-1,1)
k = 2 / 3
A = (1/(1+k))*(X + k * Y)
 
print("Vector A = " , A ) 

M = np.array([-10,14] , dtype = np.float64).reshape(-1,1)
N = np.array([10,-16] , dtype = np.float64).reshape(-1,1)

def plot_it(P,Q,str1,str2):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str1 , label =  str2)

plt.figure()

plot_it(X,Y,"g--","Line Segment XY")
plot_it(M,N,"r-","Line Containing A")
coords = np.block([[X,Y,A]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = ['X','Y','A']

for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(0,-30),
                 ha='center')
plt.xlim([-6,8])
plt.ylim([-8,0])
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.legend(loc = "best")
plt.title("Fig:4.11.10")
plt.savefig("../figs/section2.png")
plt.show()

#plt.savefig('../figs/section1.png')
#subprocess.run(shlex.split("termux-open ../figs/section1.png"))
