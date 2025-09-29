import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6), dpi=100)

x = np.array([-32/3, 0, -4])
y= np.array([0, 24/5, 3])

plt.plot(x,y,'o-', color='orange',mfc='blue',ms='15',alpha=0.5, label="Required Line")
plt.text(x[0]+0.15, y[0]+0.15, "P(-32,0)", color='blue')
plt.text(x[1]-0.25, y[1]-0.25, "Q(0,24/5)", color='blue')
plt.text(x[2]+0.15, y[2]+0.15, "R(-4,3)", color='blue')
plt.legend()
plt.title("Graph")
plt.grid()
plt.xlim(-32/3, 0)
plt.ylim(0, 24/5)

plt.savefig('figure.png', dpi=300, bbox_inches='tight')
plt.show()
