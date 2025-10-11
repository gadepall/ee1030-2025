
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA



#local imports
from line.funcs import *
from conics.funcs import *


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-8,8,len)
y2 = np.linspace(-4,4,len//2)

#conic parameters
V = np.array(([0,0],[0,1]))
u = -4*e1
f = 0

n,c,F,O,lam,P,e = conic_param(V,u,f)
#print(n,c,F)

#Eigenvalues and eigenvectors

flen = parab_param(lam,P,u)

#Standard parabola generation
x = parab_gen(y,flen)
x2 = parab_gen(y2,flen)

#Directrix
k1 = -8
k2 = 8

#Latus rectum
cl = (n.T@F).flatten()

#Generating lines
x_A = line_norm(n,c,k1,k2)#directrix
x_B = line_norm(n,cl[0],k1,k2)#latus rectum
#print(n,c)
xStandard =np.block([[x],[y]])
x2Standard =np.block([[x2],[y2]])

#Affine conic generation
Of = O.flatten()
xActual = P@xStandard + Of[:,np.newaxis]
x2Actual = P@x2Standard + Of[:,np.newaxis]
ax.fill_between(x2Actual[0,:],x2Actual[1,:],color = 'cyan')

#plotting
plt.plot(xActual[0,:],xActual[1,:],label='Parabola',color='r')
plt.plot(x_B[0,:],x_B[1,:],label='(x= 2)Latus Rectum')
#
colors = np.arange(1,3)
#Labeling the coordinates
tri_coords = np.block([O,F])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['$\\mathbf{O}$','$\\mathbf{F}$']
for i, txt in enumerate(vert_labels):
#    plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-20,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
'''
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig("../figs/img.png")
