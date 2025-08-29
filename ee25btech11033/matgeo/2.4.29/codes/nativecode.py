
import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd


A  = dst[:,0].reshape(-1,1)
B  = dst[:,1].reshape(-1,1) 
C  = dst[:,2].reshape(-1,1)

#print(A,B,C)
'''
#Triangle vertices
# The coordinates for A, B, and C have been updated.
A = np.array([2,9]).reshape(-1,1)
B = np.array([2,5]).reshape(-1,1) 
C = np.array([5,5]).reshape(-1,1) 

#Triangle sides
c = LA.norm(A-B)
a = LA.norm(B-C)
b = LA.norm(C-A)
print(a,b,c)

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
print(area)

#Angles
angA = np.degrees(np.arccos((-m1.T@m3)/(c*b)))
angB = np.degrees(np.arccos((-m1.T@m2)/(c*a)))
angC = np.degrees(np.arccos((-m2.T@m3)/(a*b)))
#print(angA,angB,angC)

#Writing sides to excel
sides=np.array([a,b,c]).reshape(-1,1)
columns=['a','b','c']

# Create DataFrame from multiple lists
df = pd.DataFrame(sides.T,columns=columns)
df.to_excel('tables/output.xlsx')
#print(df)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)



#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


plt.savefig('figs/fig.png')

plt.show()