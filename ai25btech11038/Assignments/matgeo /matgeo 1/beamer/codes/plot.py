import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points
P = (3, 2, -4)
Q = (5, 4, -6)
R = (9, 8, -10)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter points
ax.scatter(*P, color='red', label='P(3,2,-4)')
ax.scatter(*Q, color='blue', label='Q(5,4,-6)')
ax.scatter(*R, color='green', label='R(9,8,-10)')

# Line PR (whole line)
ax.plot([P[0], R[0]], [P[1], R[1]], [P[2], R[2]], color='black', linestyle='--', label='PR')

# Subsegments PQ and QR
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], color='red', linewidth=2, label='PQ')
ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]], color='green', linewidth=2, label='QR')

# Labels on points
ax.text(*P, "P", color='red')
ax.text(*Q, "Q", color='blue')
ax.text(*R, "R", color='green')

# Axis labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

plt.show()

plt.savefig('../figs/img.png')