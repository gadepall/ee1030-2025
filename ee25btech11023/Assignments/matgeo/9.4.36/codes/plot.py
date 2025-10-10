import numpy as np
import matplotlib.pyplot as plt
from call import get_data_from_c

all_data = get_data_from_c()
num_points = int(all_data[2])
roots = all_data[0:2]
parabola_points = all_data[3:].reshape((num_points, 2))

positive_root = max(roots)
fig, ax = plt.subplots(figsize=(12, 10))
ax.plot(parabola_points[:, 0], parabola_points[:, 1], 'b-', label='$y = x^2 - 4x - 21$')
ax.scatter(roots, [0, 0], color='red', s=100, zorder=5)
pointA = np.array([min(roots), 0])
pointB = np.array([max(roots), 0])

label_A = f"$\\mathbf{{A}}$\n({pointA[0]:.0f}, {pointA[1]:.0f})"
ax.annotate(label_A,
            xy=pointA,
            xytext=(-20, 5),
            textcoords='offset points',
            ha='center',
            fontsize=12)
label_B = f"$\\mathbf{{B}}$\n({pointB[0]:.0f}, {pointB[1]:.0f})"
ax.annotate(label_B,
            xy=pointB,
            xytext=(-20, 5),
            textcoords='offset points',
            ha='center',
            fontsize=12)

ax.set_title("Age of Ram",fontsize=14)
ax.set_xlabel("x",fontsize=14)
ax.set_ylabel('y',fontsize=14)

ax.grid(True)
ax.axis('equal')
ax.legend(loc='best')
plt.show()
