import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6), dpi=100)
a=0
b=0
x=np.array([-1,3,a,0])
y=np.array([1,3,b,2])
x[2]=(x[0]+x[1])/2
y[2]=(y[0]+y[1])/2

plt.scatter(x,y, color='blue', alpha=0.5, )
plt.text(x[0]+0.15, y[0]+0.15, "A(-1,1)", color='blue')
plt.text(x[1]-0.15, y[1]-0.15, "B(3,3)", color='blue')
plt.text(x[2]+0.15, y[2]+0.15, "R(1,2)", color='blue')
plt.text(x[3]+0.15, y[3]+0.15, "P(0,2)", color='blue')
plt.title("Graph")

plt.grid()
plt.plot(x,y, 'o-', color='orange', mfc='blue', ms=0,alpha=0.5, label='Line AB and PR')
plt.legend()
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
plt.show()
