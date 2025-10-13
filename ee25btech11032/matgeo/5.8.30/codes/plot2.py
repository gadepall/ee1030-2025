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

A = np.array([[60,240],[100,200]] , dtype = np.float64)
C = np.array([4,25/6], dtype = np.float64).reshape(-1,1)
sol = LA.solve(A,C)

print("Speed of Train = " , 1/sol[0])
print("Speed of Bus = " , 1/sol[1])

def plot_it(P,Q,str1,str2):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str1 , label =  str2)

plt.figure()
M = np.array([61/15,-1],dtype=np.float64).reshape(-1,1)
N = np.array([-10,151/60],dtype=np.float64).reshape(-1,1)
plot_it(M,N,"g-","Line 1 ")
M = np.array([2+1/24 , -1],dtype=np.float64).reshape(-1,1)
N = np.array([-10,5+1/48],dtype=np.float64).reshape(-1,1)
plot_it(M,N,"r-","Line 2")
plt.scatter(np.squeeze(sol[0]),np.squeeze(sol[1]))
plt.annotate(f"P\n(1/{1/np.squeeze(sol[0]):.0f},1/{1/np.squeeze(sol[1]):.0f})",(np.squeeze(sol[0]),np.squeeze(sol[1])),textcoords = "offset points" ,xytext = (0,-25),ha = "center")

plt.xlim([-1/2,1/2])
plt.ylim([-1/2,1/2])

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("5.8.30")

plt.savefig("../figs/Inter2.png")
plt.show()

#plt.savefig('../figs/Inter2.png')
#subprocess.run(shlex.split("termux-open ../figs/Inter2.png"))
