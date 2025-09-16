import math
import sys 
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen


#if using termux
#import subprocess
#import shlex

def norm_sq(P,Q) :
    return pow(LA.norm(P-Q),2)

def ratio(A,B,P,norm) :
    k =  (A[0]-P[0]) * (P[0] - B[0]) + (A[1] - P[1]) * (P[1] - B[1])
    return k /norm 


A = np.array([-4,-6]).reshape(-1,1)
B = np.array([-1,7]).reshape(-1,1)
P = np.array([-34/13 , 0 ]).reshape(-1,1)

norm = norm_sq(P,B)

k = ratio(A,B,P,norm) 
k = np.squeeze(k) 
print("Ratio = " , k ) 

def plot_it(P,Q,str):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str , label = "Line Segment AB" )

plt.figure()

plot_it(A,B,"g--")

coords = np.block([[A,B,P]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = ['A','B','P']

for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(20,15),
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.legend(loc = "best")
plt.title("Fig:4.3.21")
plt.savefig("../figs/section2.png")
plt.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))

