import matplotlib.pyplot as plt
import numpy as np
from call import send_data

a, b, c = send_data()

def parabola(x,y):
    return x**2+y**2+b*x*y+a*x+a*y+c
X, Y = np.meshgrid((np.linspace(-15, 15, 400)), (np.linspace(-15, 15, 400)))
Z = parabola(X,Y)

p = np.linspace(-10, 10, 200)
q = p

r = p = np.linspace(-10, 10, 200)
s = -r

plt.plot(p,q,"-r")
plt.plot(r,s,"-g")
plt.plot(2,2,'ko')
plt.plot(1,1,'ko')
plt.contour(X,Y,Z,levels=[0], colors = "black", linewidths = 1)
plt.text(-6.5,-5.7,"y=x",color='black',fontsize = 12)
plt.text(-7.14,7.18,"y=-x", color = 'black', fontsize = 12)
plt.text(2.52, 11.64, r'$(x+y)^2=8(x+y-2)$', color = 'black', fontsize = 12)
plt.text(2.4,2,"(2,2)", color = 'black', fontsize = 10)
plt.text(1.05,0.65, "(1,1)", color = 'black', fontsize = 10)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axvline(0, color='black', linewidth=2)
plt.axhline(0,color='black',linewidth=2)
plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/plot.png")
plt.show()