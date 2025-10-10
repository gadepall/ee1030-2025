#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
import sys                                          #for path to external scripts
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/') 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *

from call import get_line_data_from_c

P,point_a,dir_d=get_line_data_from_c()

line_points=point_a+np.array([-3,3]).reshape(-1,1)*dir_d
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111,projection='3d')

X_plane=np.linspace(-10,15,5)
Y_plane=np.linspace(-25,20,10)
X_plane,Y_plane = np.meshgrid(X_plane,Y_plane)
Z_plane=np.zeros_like(X_plane)
ax.plot_surface(X_plane,Y_plane,Z_plane,alpha=0.2,color='gray')
ax.plot(line_points[:,0],line_points[:,1],line_points[:,2],color='b',label='Line')
ax.scatter(P[0],P[1],P[2],color='r',s=35,label='Intersection Point')
ax.text(P[0],P[1],P[2]+1.2,f'P({P[0]:.0f},{P[1]:.0f},{P[2]:.0f})',ha='center')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
plt.savefig('fig1.png')
