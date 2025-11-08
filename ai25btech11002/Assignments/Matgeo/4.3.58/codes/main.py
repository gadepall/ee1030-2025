import math
#import sys   
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
#import subprocess
#import shlex
#end if
x1 = np.arange(-50,50,0.1)
y1 = -x1/3
z1 = 5*y1

x2 = np.arange(-50,50,0.1)
y2 = -2*x2
z2 = -5*x2

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#Generating the plane
x=np.arange(-50,50,0.1)
y=np.arange(-50,50,0.1)
X,Y = np.meshgrid(x,y)
Z=2*Y-X
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan')

#Plotting all lines
ax.plot(x1,y1, z1,color='pink',label='$Line 1$')
ax.plot(x2,y2, z2,color='y',label='$Line 2$')

#Setting axes' labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Points A, B, C and the line passing through')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
