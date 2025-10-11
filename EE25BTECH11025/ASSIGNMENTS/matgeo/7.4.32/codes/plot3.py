import numpy as np
import matplotlib.pyplot as plt
from call import get_results

ratio, focus, directrix_y, area, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, T1x, T1y, T2x, T2y, T3x, T3y = get_results()
A = ([Ax, Bx, Cx, Dx, Ax, Bx])
B = ([Ay, By, Cy, Dy, Ay, By])
C = ([T1x, T2x, T3x, T1x, T2x])
D = ([T1y, T2y, T3y, T1y, T2y])

triangle = np.array([[0,0], [2,0], [1, np.sqrt(3)/2]])
plt.plot(A, B, color='black')
plt.text(Ax+0.1, Ay+0.1, "A", fontsize = 10, color = 'black')
plt.text(Bx+0.1, By+0.1, "B", fontsize = 10, color = 'black')
plt.text(Cx+0.1, Cy+0.1, "C", fontsize = 10, color = 'black')
plt.text(Dx+0.1, Dy+0.1, "D", fontsize = 10, color = 'black')
plt.plot(C, D, color='black') 
plt.text(T1x+0.1, T1y+0.1, "T1", fontsize = 10, color = 'black')
plt.text(T2x+0.1, T2y+0.1, "T2", fontsize = 10, color = 'black')
plt.text(T3x+0.1, T3y+0.1, "T3", fontsize = 10, color = 'black')

plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/plot3.png")
plt.show()