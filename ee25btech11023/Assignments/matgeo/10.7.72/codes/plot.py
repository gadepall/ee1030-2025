import matplotlib.pyplot as plt
import numpy as np
from call import get_plot_data

data = get_plot_data()
P = data["p_fixed"]
P1, T1, T2 = data["p1"], data["t1"], data["t2"]
P2, T3, T4 = data["p2"], data["t3"], data["t4"]
a, b, c = data["line_coeffs"]

fig, ax = plt.subplots(figsize=(9, 9))

circle = plt.Circle((0, 0), 1, color='blue', fill=False, label='$x^2+y^2=1$')
ax.add_patch(circle)
x_vals = np.array([-1, 4])
y_vals = (-a * x_vals - c) / b
ax.plot(x_vals, y_vals, 'g-', label=f'${int(a)}x+{int(b)}y={int(-c)}$')

ax.plot([P1[0], T1[0]], [P1[1], T1[1]], 'r--', alpha=0.7)
ax.plot([P1[0], T2[0]], [P1[1], T2[1]], 'r--', alpha=0.7)
ax.plot([T1[0], T2[0]], [T1[1], T2[1]], 'r-', label='Chord 1')

ax.plot([P2[0], T3[0]], [P2[1], T3[1]], 'm--', alpha=0.7)
ax.plot([P2[0], T4[0]], [P2[1], T4[1]], 'm--', alpha=0.7)
ax.plot([T3[0], T4[0]], [T3[1], T4[1]], 'm-', label='Chord 2')

ax.scatter([P1[0], P2[0]], [P1[1], P2[1]], color='orange', s=50, zorder=5)
ax.text(P1[0] - 0.4, P1[1], '$P_1$')
ax.text(P2[0] + 0.2, P2[1], '$P_2$')

ax.scatter(P[0], P[1], color='black', s=120, zorder=5, label='Fixed Point')
ax.text(P[0] + 0.1, P[1] - 0.2, f'({P[0]:.2f}, {P[1]:.2f})')

ax.set_title('Chords of Contact Through a Fixed Point',fontsize=14)
ax.set_xlabel('X-axis',fontsize=14); ax.set_ylabel('Y-axis',fontsize=14)

ax.grid(True); ax.axis('equal')
ax.set_xlim(-2.5, 4.5); ax.set_ylim(-2.5, 4.5)
ax.legend()
plt.show()
