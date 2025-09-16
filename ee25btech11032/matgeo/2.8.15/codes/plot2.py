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

l = np.cos(np.deg2rad(60))
m = np.cos(np.deg2rad(45))
n = np.sqrt(1 - l**2 - m**2)
print(n)
l *= 10
m *= 10
n *= 10

A1 = np.array([l,m,n]).reshape(-1,1)
A2 = np.array([l,m,-n]).reshape(-1,1)
O = np.array([0,0,0]).reshape(-1,1)

def plot_it(P,Q,str):
    x_l = line_gen_num(P,Q,20)
    ax.plot(x_l[0,:],x_l[1,:],x_l[2,:] , str )

fig = plt.figure()
ax = fig.add_subplot(111,projection = "3d")

plot_it(A1,O,"g-")
plot_it(A2,O,"r-")

coords = np.block([[A1,A2,O]])
plt.scatter(coords[0,:],coords[1,:],coords[2,:])
vert_labels = [r'$A_1$',r'$A_2$','O']
for i, txt in enumerate(vert_labels):
    if (coords[0,i] == 0 ) :
        ax.text(coords[0,i], coords[1,i] , coords[2,i],txt , ha='center', va = 'bottom')
    else :
        ax.text(coords[0,i], coords[1,i] , coords[2,i],f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f}, {coords[2,i]:.1f})',ha='center', va = 'bottom')

ax.scatter(coords[0,2], coords[1,2], coords[2,2], color="b", label="O : ORIGIN")
ax.legend(loc = "best")


ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
#plt.legend(loc='best')
ax.grid()
ax.set_xlim([-2, 7])
ax.set_ylim([-2,8])
ax.set_zlim([-6,6])
plt.title("Fig:2.8.15")
#ax.set_box_aspect([1,1,1])

fig.savefig("../figs/vector2.png")
fig.show()
#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))

