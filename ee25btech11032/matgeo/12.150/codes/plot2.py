import math
import sys
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from line.funcs import *

a = np.array([1, 1, 1])
b = np.array([-1, -1, 1])
c = np.cross(a, b)

a=a.reshape(-1,1)
b=b.reshape(-1,1)
c=c.reshape(-1,1)

def plot_it(P,Q,str1,str2):
    x_l = line_gen_num(P,Q,20)
    ax.plot(x_l[0,:],x_l[1,:],x_l[2,:] , str1, label = str2 )

origin = np.zeros(3).reshape(-1,1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
plot_it(origin,a,"r","side a")
plot_it(origin,b,"orange","side b")
plot_it(origin,c,"g","")
plot_it(a,b,"b","side a+b")
'''
# Define triangle vertices (O, a, b)
triangle = np.array([origin, a, b])
ax.add_collection3d(Poly3DCollection([triangle], alpha=0.4, facecolor='orange'))'''


coords = np.block([[a,b,c,origin]])
plt.scatter(coords[0,:],coords[1,:],coords[2,:])
vert_labels = [r'$a$',r'$b$',r'$a\times b$',"O"]
for i, txt in enumerate(vert_labels):
   ax.text(coords[0,i], coords[1,i] , coords[2,i],f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f}, {coords[2,i]:.1f})',ha='center', va = 'bottom')

ax.scatter(coords[0,3], coords[1,3], coords[2,3], color="b", label="O : ORIGIN")


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc = "best")
ax.legend(loc='upper left', bbox_to_anchor=(.90, 1.10))
ax.grid()
plt.title("Fig:12.150")
ax.set_box_aspect([1,1,1])

fig.savefig("../figs/vector2.png")
fig.show()
#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))

