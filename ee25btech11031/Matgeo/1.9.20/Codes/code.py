import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
import ctypes

c_lib=ctypes.CDLL('./code.so')

c_lib.Solve_for_y.argtypes = [
        ctypes.c_double*2,
        ctypes.c_double*2
        ]

c_lib.Solve_for_y.restype = ctypes.c_double

A_c = (ctypes.c_double*2)(5.0, -2.0) #in order for the C function to recognise the points as doubles(the given input type) and not numpy arrays. 
B_c = (ctypes.c_double*2)(-3.0, 2.0)

y = c_lib.Solve_for_y(A_c,B_c)

A = np.array([5,-2]).reshape(-1,1) #we have done reshape, so henceforth, A will be treated as a column vector ONLY. 
B = np.array([-3,2]).reshape(-1,1)

P = np.array([0,y]).reshape(-1,1)

plt.plot([P[0,0], B[0,0]], [P[1,0], B[1,0]], label="Line Segment $PB$")
plt.plot([P[0,0], A[0,0]], [P[1,0], A[1,0]], label="Line Segment $PA$")


#Labeling the coordinates
tri_coords = np.block([[A,B,P]]) #A,B,P are column vectors. We are stacking them side by side (as a block), creating a 2-D array called tri_coords. 

plt.scatter(tri_coords[0,:], tri_coords[1,:]) #accessing the values we put in tri_coords to get x coordinates in first step and y coordinates in the next. 

vert_labels = ['A','B','P'] #storing labels of points in an array
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')


plt.savefig("../Figs/plot(py+C).png")

plt.show()

