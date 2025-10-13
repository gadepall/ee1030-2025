import math
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *
m = 10 
X = np.linspace(58-m,58+m,num=4)
Y1 = (11-2*X)/3
Y2 = (-24-2*X)/4
Y3 = (-19/29)*X+3


plt.plot(X,Y1,label="2x+3y=11",color="red")
plt.plot(X,Y2,label="2x+4y=-24")
plt.plot(X,Y3,label="y = mx +3",color = "green")
plt.scatter([58],[-35])
plt.text(58,-35,"X")

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.savefig('../figs/img.png')
