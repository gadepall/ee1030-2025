import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5), dpi=200)
plt.xlim(-1,4)
plt.ylim(-1,4)
A=np.array([[3,6],[4,2]])
c=np.array([6,5])

an=np.linalg.inv(A)
ans=np.dot(an,c)

Ans=np.linalg.solve(A,c)
print("x=",Ans[0],"y=",Ans[1])
a=1/ans[0]
b=1/ans[1]

x = np.array([a,b]).reshape(-1,1)

x1= np.linspace(-1,4,100)
l1= (6*x1)/(6*x1-3)
l2= (2*x1)/(5*x1-4)

plt.plot(x1,l1, color='blue', label="Conic 1")
plt.plot(x1,l2, color='orange', label="Conic 2")
plt.scatter(1,2, c='r', zorder=5)
plt.text(1,2,"(1,2)")
plt.text(0,0,"Origin",)


plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.savefig("figure.png", dpi=200)
plt.show()

