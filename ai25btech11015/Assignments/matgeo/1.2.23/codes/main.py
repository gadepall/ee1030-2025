import matplotlib.pyplot as plt
import numpy as np 

# Code by M SAI RITHIK
# 1.2.23 Represent graphically a displacement
# of 40 km, 30◦ west of south.
# (−20, −20 √3)


coords = np.loadtxt('var.dat', delimiter=' ')
point = np.array(coords) * 40

origin = np.array([0,0])

vec = np.array([origin,point])


plt.plot(vec[:,0], vec[:,1], color="red",label="AB")
plt.scatter(vec[:,0], vec[:,1],color = "red")
plt.title("Displacement Vector")

plt.text(vec[0,0],vec[0,1],"A")
plt.text(vec[1,0],vec[1,1],"B")

plt.axhline(0, color='black')   # x-axis
plt.axvline(0, color='black')   # y-axis
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.legend(loc="best")
plt.savefig('../figs/fig.png', dpi=300)
