import numpy as np
import matplotlib.pyplot as plt
from call import get_results

ratio, focus, directrix_y, area, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, T1x, T1y, T2x, T2y, T3x, T3y = get_results()
A = ([Ax, Bx, Cx, Dx, Ax, Bx])
B = ([Ay, By, Cy, Dy, Ay, By])

x = np.linspace(-5, 5, 300)

p = focus[1] - directrix_y
y = (x**2) / (4*p)
plt.plot(x, y, label="Locus (Parabola)")
plt.axhline(directrix_y, color='r', linestyle='--', label='Directrix')
plt.plot(focus[0], focus[1], 'go')
plt.plot(A, B, color='black')
plt.text(Ax+0.1, Ay+0.1, "A", fontsize = 10, color = 'black')
plt.text(Bx+0.1, By+0.1, "B", fontsize = 10, color = 'black')
plt.text(Cx+0.1, Cy+0.1, "C", fontsize = 10, color = 'black')
plt.text(Dx+0.1, Dy+0.1, "D", fontsize = 10, color = 'black')
plt.text(focus[0]+0.1, focus[1]+0.1, 'focus', fontsize = 10, color = 'black')

plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/plot2.png")
plt.show()
