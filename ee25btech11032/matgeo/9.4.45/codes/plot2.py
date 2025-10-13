import math
import sys 
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

from line.funcs import *
from conics.funcs import *

a, b, c = 1, 48,-324  


roots = np.roots([a, b, c])
for i in roots : 
    if i >= 0 :
        print("Speed of Stream : " ,i)

def plot_it(P,Q,str1):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str1 , label = "Line" )

plt.figure()
P = np.array([-5,12],dtype=np.float64).reshape(-1,1)
S = np.array([10,-18],dtype=np.float64).reshape(-1,1)

plot_it(S,P,"b")

T1 = np.array([1,0],dtype=np.float64).reshape(-1,1)
T2 = np.array([0,2],dtype=np.float64).reshape(-1,1)

coords = np.block([[T1,T2]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = [r't_1',r't_2']

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel('$Time: Downstream$')
plt.ylabel('$Time: Upstream$')

plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.xlim([-2,4])
plt.ylim([-2,4])
plt.title("9.4.45 - 1 ")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph2_1.png")
#plt.show()
plt.figure()
x = np.linspace(-100,100,400)
y = a*x**2 + b*x + c

plt.plot(x,y,"b",label="Parabola")


T1 = np.array([6,0],dtype=np.float64).reshape(-1,1)
T2 = np.array([-54,0],dtype=np.float64).reshape(-1,1)

coords = np.block([[T1,T2]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = [r'k_1',r'k_2']

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
plt.grid(True) 
plt.axis('equal')
plt.xlim([-60,20])
plt.ylim([-20, 20 ])
plt.title("9.4.45 - 2 ")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph2.2.png")
