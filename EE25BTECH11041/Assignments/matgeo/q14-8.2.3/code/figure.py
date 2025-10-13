import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(-7,7,200)
x = -y*y/8

plt.axvline(x=2, color='blue', label="Directrix")
plt.axvline(x=-2, color='orange', label="Latus Rectum")

xp = np.array([0,2,-2])
yp = np.array([0,0,0])
plt.scatter(xp,yp)


plt.annotate('O', xy=(0, 0)) 
plt.annotate('F', xy=(-2, 0), xytext=(-1.7,0.5)) 

plt.plot(x,y, label="Parabola", color='red')
plt.grid()
plt.legend()
plt.savefig("figure.png", dpi=300)
plt.show()
