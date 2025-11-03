import numpy as np
import matplotlib.pyplot as plt
from call import get_data_from_c
all_data = get_data_from_c()
num_points = 51

focus = all_data[0:2]
parabola_orig = all_data[2 : 2 + num_points*2].reshape((num_points, 2))
parabola_locus = all_data[2 + num_points*2 :].reshape((num_points, 2))

P1 = parabola_orig[35]
P2 = parabola_orig[15]
M1 = parabola_locus[35]
M2 = parabola_locus[15]
fig, ax = plt.subplots(figsize=(12, 10))

ax.plot(parabola_orig[:, 0], parabola_orig[:, 1], 'b-', label='$y^2=4ax(a=2)$')
ax.plot(parabola_locus[:, 0], parabola_locus[:, 1], 'r-', label='Locus(Midpoint) Parabola')
ax.text(8.2, 8.2,'$y^2=8x$', color='b')
ax.axvline(x=0, color='g', linestyle='--', label='Directrix of Locus (x=0)')
ax.scatter(focus[0], focus[1], color='black', s=100, zorder=5, label='Focus (F)')
ax.text(focus[0] + 0.2, focus[1] + 0.2, 'F(2,0)')

ax.plot([focus[0], P1[0]], [focus[1], P1[1]], color='b', linestyle='--')
ax.plot([focus[0], P2[0]], [focus[1], P2[1]], color='b', linestyle='--')
ax.scatter(P1[0], P1[1], color='b', s=50, zorder=5)
ax.text(P1[0] + 0.2, P1[1], '$P_1$', fontsize=12, color='b')

ax.scatter(P2[0], P2[1], color='b', s=50, zorder=5)
ax.text(P2[0] + 0.2, P2[1], '$P_2$', fontsize=12, color='b')
ax.scatter(M1[0], M1[1], color='red', s=50, zorder=5)
ax.text(M1[0] - 0.7, M1[1], '$M_1$', fontsize=12, color='red')

ax.scatter(M2[0], M2[1], color='red', s=50, zorder=5)
ax.text(M2[0] - 0.7, M2[1], '$M_2$', fontsize=12, color='red')
ax.text(0.17, -7,'$x=0$', color='g')

ax.set_title('Locus of the Midpoint',fontsize=14)
ax.set_xlabel('X-axis',fontsize=12)
ax.set_ylabel('Y-axis',fontsize=12)

ax.grid(True)
ax.axis('equal')
ax.legend()
plt.show()
