import math
import sys #for path to external scripts
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo') #path to my scriptsi
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
#import subprocess
#import shlex

def func(P, B):
    # NumPy automatically applies operations to each element in the array
    return 2*P -B

def func_radius(P,B) :
    return LA.norm(P-B)

P = np.array([-2,2]).reshape(-1,1)
B = np.array([3,4]).reshape(-1,1)

A = func(P,B).reshape(-1,1)

x_AB = line_gen_num(A,B,20)
radius = func_radius(P,B)
print(x_AB)
x_circ = circ_gen(P,radius)
plt.plot(x_circ[0,:],x_circ[1,:],"red",label="Circle")

plt.plot(x_AB[0,:],x_AB[1,:],"g--",label="Diameter")
tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = [f'A({A[0]},{A[1]})','B','P']
for i , txt in enumerate(vert_labels):
    plt.annotate(txt,(tri_coords[0,i],tri_coords[1,i]),textcoords="offset points", xytext=(0,10),ha='right')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.title("1.5.20")
plt.axis('equal')
plt.savefig("../figs/circle_graph2.png")
plt.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))

