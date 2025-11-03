
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


a,b,k= 1,2,3
theta = np.linspace(0,2*np.pi,100)
Y = np.sin(theta)*k 
X = np.cos(theta)*k 
plt.plot(X,Y)


Y=np.linspace(-2,5+7/4,5)

X = (a**2+b**2+k**2-2*b*Y)/(2*a)
plt.scatter(X,Y,color="cyan")
plt.plot(X,Y,color="cyan",label="Locus")
plt.scatter(0,0,label="Given circle")

for y in Y:
    x = (a**2+b**2+k**2-2*b*y)/(2*a)
    r = np.sqrt(x**2+y**2 - k**2)

    X0=np.array([x,y]).reshape(-1,1)


    Y2 = np.sin(theta)*r +y
    X2 = np.cos(theta)*r +x
    plt.plot(X2,Y2)



plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig("../figs/img2.png")

