import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-8,2,300)
y=6*x*x+37*x+6

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
xp = np.array([-6, -1/6])
yp=np.array([0,0])


plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')

plt.grid()
plt.plot(x,y, label='Quadratic')

plt.scatter(xp,yp, label='roots', color='orange')
plt.legend()
plt.text(xp[0]+0.05, yp[0]+0.05, "(-6,0)")
plt.text(xp[1]+0.05, yp[1]+0.05, "(-1/6,0)")

plt.savefig("figure.png", dpi=300)
plt.show()
