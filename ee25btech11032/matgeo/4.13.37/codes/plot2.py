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

O = np.zeros(2).reshape(-1,1)
A = np.array([1,2]).reshape(-1,1)
B = np.zeros(2).reshape(-1,1)
C = np.zeros(2).reshape(-1,1)
r = 3 
B = r * A
C = (r ** 2 ) *A

print("Vector A = " , A)
print("Vector B = " , B)
print("Vector C = " , C)

def plot_it(P,Q,str1,str2):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str1 , label =  str2)

plt.figure()
plot_it(O,A,"g-"," Line Segment : OA ")
plot_it(A,B,"r-"," Line Segment : AB ")
plot_it(B,C,"b-"," Line Segment : BC ")

coords = np.block([[A,B,C,O]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['A','B','C','O']

for i , txt in enumerate(vert_label) :
    
    if i != 2 :
        plt.annotate(f"{txt}\n({coords[0,i]:.1f},{coords[1,i]:.1f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,12),ha = "center")
    else :
        plt.annotate(f"{txt}\n({coords[0,i]:.1f},{coords[1,i]:.1f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("4.13.37")

plt.savefig("../figs/colli2.png")
plt.show()

#plt.savefig('../figs/colli2.png')
#subprocess.run(shlex.split("termux-open ../figs/colli2.png"))
