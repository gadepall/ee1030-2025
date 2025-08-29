import math
import sys 
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen


#if using termux
#import subprocess
#import shlex

def length(P,Q) :
    return LA.norm(P-Q)

A = np.array([-2,1]).reshape(-1,1)
B = np.array([1,0]).reshape(-1,1)
C = np.array([4,1]).reshape(-1,1)
D = np.array([1,2]).reshape(-1,1)

d1 = length(A,B)
d2 = length(B,C)
if d1 != d2 :
    print("Length of AB and CD = ",d1)
    print("Length of BC and AD = ",d2)
else :
    print("Length of all sides = ",d1)


def plot_it(P,Q,str):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str )

plt.figure()

plot_it(A,B,"g-")
plot_it(B,C,"r-")
plot_it(C,D,"b-")
plot_it(D,A,"y-")


coords = np.block([[A,B,C,D]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = ['A','B','C','D']
#for i , txt in enumerate(vert_labels):
 #   plt.annotate(txt,(coords[0,i],coords[1,i]),textcoords="offset points", xytext=(0,10),ha='center')
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.0f}, {coords[1,i]:.0f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(20,0),
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid()

plt.title("Fig:1.9.21")
plt.axis('equal')

plt.savefig("../figs/p_gram2.png")
plt.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))

