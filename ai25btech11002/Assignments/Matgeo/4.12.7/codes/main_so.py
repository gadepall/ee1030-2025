
import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
import ctypes

# Load shared library
lib = ctypes.CDLL("./libcoords.so")

# Define argument and return types
lib.polar_to_cartesian.argtypes = [ctypes.c_double, ctypes.c_double,
                                   ctypes.POINTER(ctypes.c_double),
                                   ctypes.POINTER(ctypes.c_double)]
lib.polar_to_cartesian.restype = None

# Example: C coordinates
x = ctypes.c_double()
y = ctypes.c_double()
lib.polar_to_cartesian(6.0, 60.0, ctypes.byref(x), ctypes.byref(y))

'''
#Input parameters from excel file
df= pd.read_excel('tables/vertices.xlsx')
#print(df)
dst = df.to_numpy()[:,:]
print(dst)

A  = dst[:,0].reshape(-1,1)
B  = dst[:,1].reshape(-1,1) 
C  = dst[:,2].reshape(-1,1)

#print(A,B,C)
'''
#Triangle vertices
A = np.array([5,0]).reshape(-1,1)
B = np.array([0,0]).reshape(-1,1) 
C = np.array([x.value,y.value]).reshape(-1,1) 

#Triangle sides
c = LA.norm(A-B)
a = LA.norm(B-C)
b = LA.norm(C-A)
#print(a,b,c)

#Direction Vectors
m1 = dir_vec(A,B)
m2 = dir_vec(B,C)
m3 = dir_vec(C,A)
#print(m1,m2,m3)

#Line parameters
n1 = norm_vec(A,B)
c1 = n1.T@A
n2 = norm_vec(B,C)
c2 = n2.T@B
n3 = norm_vec(C,A)
c3 = n3.T@C
#print(n1,c1,n2,c2,n3,c3)

#Area
arvec = np.cross(m1[:,0],m3[:,0])
area = 1/2*LA.norm(arvec)
#print(area)

#Angles
angA = np.degrees(np.arccos((-m1.T@m3)/(c*b)))
angB = np.degrees(np.arccos((-m1.T@m2)/(c*a)))
angC = np.degrees(np.arccos((-m2.T@m3)/(a*b)))
#print(angA,angB,angC)

#Writing sides to excel
sides=np.array([a,b,c]).reshape(-1,1)
columns=['a','b','c']

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)



#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../Figs/plot.png')
plt.show()
#else
#plt.show()

