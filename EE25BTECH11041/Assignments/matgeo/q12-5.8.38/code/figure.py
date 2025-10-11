import numpy as np
import matplotlib.pyplot as plt

c=np.array([42,-6])
a= np.array([[7,-1],[3,-1]])

inv=np.linalg.inv(a)

ans=np.dot(inv,c)

print("x=", ans[0],"y=",ans[1])

x=np.linspace(9,15,200)
l1=7*x-42
l2=3*x+6



plt.plot(x,l1, label="line 1, 7x-y=42")
plt.plot(x,l2,label="line 2, 3x-y=-6")
plt.scatter(12,42, c='r', zorder=5)
plt.text(12.3,41, "(x,y)")
plt.xlabel("daughter's age")
plt.ylabel("Alwar's age")
plt.legend()
plt.grid()
plt.savefig("figure.png", dpi=200)
plt.show()
