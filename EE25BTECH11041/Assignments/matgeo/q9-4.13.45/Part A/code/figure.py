import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6), dpi = 200)


abX= np.array([5,2])
abY= np.array([-1,-3])
acX= np.array([5,2])
acY=np.array([-1,-3])
bcX=np.array([2,2])
bcY=np.array([-3,-3])
obx=np.array([0,2])
oby=np.array([0,-3])


plt.plot(abX,abY, ':r',marker='o', label="Line AB")
plt.plot(bcX,bcY, ':b',marker='o', label="Line BC")
plt.plot(acX,acY, ':',marker='o', color='orange', label="Line AC")
plt.plot(obx,oby, '-', color='pink', label="Line OB")


plt.annotate("A",xy=(abX[0], abY[0]))
plt.annotate("B",xy=(abX[1]+0.05, abY[1]-0.02))
plt.annotate("C",xy=(abX[1]+0.05, abY[1]+0.1))

plt.title("Graph")
plt.legend()
plt.grid()
plt.savefig("Figure.png", dpi=200)
plt.show()
