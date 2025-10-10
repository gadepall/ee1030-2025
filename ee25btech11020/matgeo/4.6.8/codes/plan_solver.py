import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libplane.so")  

lib.plane_from_points.argtypes = [ctypes.POINTER(ctypes.c_double),
                                  ctypes.POINTER(ctypes.c_double),
                                  ctypes.POINTER(ctypes.c_double),
                                  ctypes.POINTER(ctypes.c_double)]
lib.parallel_plane_through_point.argtypes = [ctypes.POINTER(ctypes.c_double),
                                             ctypes.POINTER(ctypes.c_double),
                                             ctypes.POINTER(ctypes.c_double)]

A = [2,2,-1]
B = [3,4,2]
C = [7,0,6]
D = [4,3,1]

P1=(ctypes.c_double*3)(*A)
P2=(ctypes.c_double*3)(*B)
P3=(ctypes.c_double*3)(*C)
coeff=(ctypes.c_double*4)()
lib.plane_from_points(P1,P2,P3,coeff)
plane1 = np.array(coeff[:])

coeff_c = (ctypes.c_double*4)(*plane1)
D_c = (ctypes.c_double*3)(*D)
coeff2=(ctypes.c_double*4)()
lib.parallel_plane_through_point(coeff_c,D_c,coeff2)
plane2 = np.array(coeff2[:])
a,b,c,d1 = plane1
a2,b2,c2,d2 = plane2

xx,yy = np.meshgrid(np.linspace(0,8,30), np.linspace(0,8,30))
zz1 = (d1 - a*xx - b*yy)/c
zz2 = (d2 - a2*xx - b2*yy)/c2

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.view_init(elev=30, azim=75) 

ax.plot_surface(xx,yy,zz1,alpha=0.5,color='blue')
ax.plot_surface(xx,yy,zz2,alpha=0.5,color='green')

points = np.array([A,B,C,D])
labels = ["A","B","C","D"]
for (x,y,z),label in zip(points,labels):
    ax.scatter(x,y,z,color='red',s=50)
    ax.text(x,y,z,label,color='black')

ax.text(1,1,(d1 - a*1 - b*1)/c,"Plane 1",color='blue')
ax.text(1,2,(d2 - a2*1 - b2*2)/c2,"Plane 2",color='green')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.savefig("../figs/img1.png")

