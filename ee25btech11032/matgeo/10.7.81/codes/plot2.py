import math
import sys
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from line.funcs import *
from conics.funcs import *

P = np.array([15,-50/3],dtype=np.float64).reshape(-1,1)
Q = np.array([-15,70/3],dtype=np.float64).reshape(-1,1)
T = np.array([1,2],dtype=np.float64).reshape(-1,1)
U = np.array([4/5,3/5],dtype=np.float64).reshape(-1,1)
O1 = T + 5 * U 
O2 = T  - 5 * U
print(O1,O2)
x_PQ = line_gen_num(P,Q,20)
x_cir1 = circ_gen(O1,5)
x_cir2 = circ_gen(O2,5)

plt.figure()

plt.plot(x_PQ[0,:],x_PQ[1,:],"g",label="Tangent")
plt.plot(x_cir1[0,:],x_cir1[1,:],"r",label="Circle 1")
plt.plot(x_cir2[0,:],x_cir2[1,:],"b",label="Circle 2")
coords = np.block([[T,O1,O2]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['P',r'$O_1$',r'$O_2$']

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
plt.xlim([-10,10])
plt.ylim([-10,12])
plt.title("10.7.81")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph2.png")
plt.show()
plt.show()
