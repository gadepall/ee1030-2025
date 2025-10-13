import numpy as np
import matplotlib.pyplot as plt
from call import get_results

ratio, focus, directrix_y, area, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, T1x, T1y, T2x, T2y, T3x, T3y = get_results()



theta = np.linspace(0, 2*np.pi, 200)
A = ([Ax, Bx, Cx, Dx, Ax, Bx])
B = ([Ay, By, Cy, Dy, Ay, By])

plt.plot(A, B, color='black')
plt.text(Ax+0.1, Ay+0.1, "A", fontsize = 10, color = 'black')
plt.text(Bx+0.1, By+0.1, "B", fontsize = 10, color = 'black')
plt.text(Cx+0.1, Cy+0.1, "C", fontsize = 10, color = 'black')
plt.text(Dx+0.1, Dy+0.1, "D", fontsize = 10, color = 'black')
plt.plot(np.cos(theta), np.sin(theta), label="Inner Circle C1")
plt.plot(np.sqrt(2)*np.cos(theta), np.sqrt(2)*np.sin(theta), label="Outer Circle C2")

plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/plot1.png")
plt.show()
