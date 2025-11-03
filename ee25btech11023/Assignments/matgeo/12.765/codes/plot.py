import matplotlib.pyplot as plt
import numpy as np
from call import solve_least_squares

v1, v2, e, alpha = solve_least_squares()

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r')
ax.text(v1[0], v1[1], v1[2], ' $\\vec{v_1}$')

line_v2 = np.array([np.zeros(3), 1.5 * v2])
ax.plot(line_v2[:, 0], line_v2[:, 1], line_v2[:, 2], 'g--', alpha=0.5 )
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g')
ax.text(v2[0], v2[1], v2[2], ' $\\vec{v_2}$')
projection_point = alpha * v2
ax.quiver(projection_point[0], projection_point[1], projection_point[2],
          e[0], e[1], e[2],
          color='k', linestyle=':' )
ax.text(projection_point[0]+0.8, projection_point[1]-0.5, projection_point[2]+0.5, '$\\vec{e}$')

# --- Formatting ---
ax.set_title('Error Vector',fontsize=14)
ax.set_xlabel('X',fontsize=12); ax.set_ylabel('Y',fontsize=12); ax.set_zlabel('Z',fontsize=12)
ax.grid(True)
ax.axis('equal')
plt.show()
