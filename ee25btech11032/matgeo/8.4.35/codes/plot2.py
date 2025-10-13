import math
import sys 
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

from line.funcs import *
from conics.funcs import *

def plot_it(P,Q,str1):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str1 )

plt.figure()

P = np.array([3,2],dtype=np.float64).reshape(-1,1)
T = np.array([-3,2],dtype=np.float64).reshape(-1,1)
R = np.array([3,-2],dtype=np.float64).reshape(-1,1)
S = np.array([-3,-2],dtype=np.float64).reshape(-1,1)

x_el = ellipse_gen(3,2)

plt.plot(x_el[0,:],x_el[1,:],"r",label = "Ellipse 1")

x_el2 = ellipse_gen((12**0.5),(16**0.5))

plt.plot(x_el2[0,:],x_el2[1,:],"g",label = "Ellipse 2")


plot_it(P,T,"b")
plot_it(T,S,"b")
plot_it(P,R,"b")
plot_it(S,R,"b")

Q = np.array([0,4],dtype=np.float64).reshape(-1,1)

coords = np.block([[P,T,R,S,Q]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['P','M','R','S','Q']

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
#plt.xlim([-10/2,10/2])
#plt.ylim([-10/2,10/2])
plt.title("8.4.35")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph2.png")
plt.show()

