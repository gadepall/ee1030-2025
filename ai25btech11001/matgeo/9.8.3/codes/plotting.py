
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


a,b,k= 1,2,3
y=0
x = (a**2+b**2+k**2-2*b*y)/(2*a)
r = np.sqrt(x**2+y**2 - k**2)

X0=np.array([x,y]).reshape(-1,1)

theta = np.linspace(0,2*np.pi,100)
Y = np.sin(theta)*k 
X = np.cos(theta)*k 

Y2 = np.sin(theta)*r +y
X2 = np.cos(theta)*r +x
plt.plot(X,Y)
plt.plot(X2,Y2)
a = (y**2+x**2)
b = -y*2*(k**2)
c = k**4 - x**2*k**2
y1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)

x1=np.sqrt(k**2 - y1**2)
X = np.linspace(x1,x,100)
X2 = np.linspace(0,x1,100)
X3 = np.linspace(0,x,100)
Y3 = 0*X3
Y = (X-x)*(y1-y)/(x1-x) +y
Y2 = (X2)*(y1)/(x1) 
plt.plot(X,Y,label="r")
plt.plot(X2,Y2,label="k")
plt.plot(X3,Y3,label="||$\\mathbf{X_0}$||")
plt.annotate('$\\mathbf{\\alpha}$',
                 (x1, y1), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,-15), # distance from text to points (x,y)
                 ha='center')



plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig("../figs/img.png")
