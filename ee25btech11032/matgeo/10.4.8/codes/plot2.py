import math
import sys 
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

from line.funcs import *
from conics.funcs import *

a, b, c = 1, -2 , 1  


roots = np.roots([a, b, c])
if roots[0] == roots[-1] : 
    print("Line is Tangent!")
else :
    print("Line is NOT Tangent!")

def plot_it(P,Q,str1):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str1 , label = "Line" )

plt.figure()
P = np.array([-10,-9],dtype=np.float64).reshape(-1,1)
S = np.array([20,21],dtype=np.float64).reshape(-1,1)

plot_it(S,P,"g")


y = np.linspace(-10,10,400)

x = parab_gen(y,1)

plt.plot(x,y,"r",label="Parabola")

T1 = np.array([1,2],dtype=np.float64).reshape(-1,1)

coords = np.block([[T1]])

plt.scatter(coords[0,:] , coords[1,:], label = "Point of Tangancy")
vert_label = ['Q']

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
plt.xlim([-2,10])
plt.ylim([-8,8])
plt.title("10.4.8")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph2.png")
plt.show()
