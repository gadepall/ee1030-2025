import math
import sys
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
#import numpy.linalg as LA
import matplotlib.pyplot as plt

from line.funcs import *

#if using termux
#import subprocess
#import shlex

A = np.array([2,3]).reshape(-1,1)
B = np.array([3,-1]).reshape(-1,1)
P = np.array([5,2]).reshape(-1,1)
K = (B-A).T

x = np.dot(K,P)
x = np.squeeze(x)
print("Required Line Equation : ")
print(K,"X = ", x )

def plot_it(P,Q,str1, str2):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] ,str1 , label = str2 )

plt.figure()

plot_it(P,(10 * A+ 7 * B)/17,"g-","Required Line")
plot_it(A,B,"r--" , "Line AB")

coords = np.block([[A,B,P, (10 * A+ 7 * B)/17 ]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = ['A','B','P','Q']

for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(25,-12),
                 ha='center', va = 'bottom')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.title("Fig:4.7.24")
plt.axis('equal')

plt.savefig("../figs/perpendicular1.png")
plt.show()

#plt.savefig('../figs/perpendicular1.png')
#subprocess.run(shlex.split("termux-open ../figs/perpendicular1.png"))


