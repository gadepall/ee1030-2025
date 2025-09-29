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

A = np.array([[3,4],
              [2,-2]], dtype = np.float64)
C = np.array([10,2] , dtype = np.float64).reshape(-1,1)

X = LA.solve(A,C)
print("Vector X = " , X ) 

def plot_it(P,Q,str1,str2):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str1 , label =  str2)

plt.figure()
P = np.array([6,-2], dtype = np.float64).reshape(-1,1)
Q = np.array([-6,7], dtype = np.float64).reshape(-1,1)
plot_it(P,Q,"g-"," Line 1 ")
P = np.array([8,7], dtype = np.float64).reshape(-1,1)
Q = np.array([-8,-9], dtype = np.float64).reshape(-1,1)
plot_it(P,Q,"r-"," Line 2 ")
plt.scatter(X[0,0], X[1,0])
plt.annotate(f"X\n({X[0,0]},{X[1,0]})",
                    (X[0], X[1]),
                    textcoords = "offset points" ,
                    xytext = (0,12),ha = "center")
plt.xlim([-1,4])
plt.ylim([-1,4])
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("5.2.35")

plt.savefig("../figs/intersect2.png")
plt.show()

#plt.savefig('../figs/intersect2.png')
#subprocess.run(shlex.split("termux-open ../figs/intersect2.png"))
