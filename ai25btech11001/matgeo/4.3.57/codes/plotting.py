import math
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *
a,d,a2,d2=0,2*5,8,4
b,c,b2=0,5*5,10

x = np.linspace(-100,100,10)
y = (x-a+d)/(a2-d2)*a2+a
z = (x-a+d)/(a2-d2)*(a2+d2)+a+d
y2 = (x-b+c)/(b2-d2)*b2+b
z2 = (x-b+c)/(b2-d2)*(b2+d2)+b+c
y_ = x.copy();
X,Y = np.meshgrid(x,y)
Z = -X+2*Y
fig = plt.figure()

ax = fig.add_subplot(111,projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.2)

y3 = a + ((a-b)/(a-d-b+c))*(x-a+d)
z3 = a+d + ((a+d-b-c)/(a-d-b+c))*(x-a+d)


# and plot the point 
ax.plot(x,y ,z,  color='green',label=f"line 1")
ax.plot(x,y2 ,z2,  color='blue',label="line 2")
ax.plot(x,y3 ,z3,  color='red',label = "line joining the point in the equation" )
plt.legend(loc='best')
plt.savefig('../figs/img.png')
