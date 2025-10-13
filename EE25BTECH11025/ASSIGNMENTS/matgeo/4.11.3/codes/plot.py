import numpy as np
import matplotlib.pyplot as plt
from call import get_data

P0, P1, Q1, Q2, Q3, X = get_data()
P0 = np.asarray(P0); P1 = np.asarray(P1)
Q1 = np.asarray(Q1); Q2 = np.asarray(Q2); Q3 = np.asarray(Q3)
X  = np.asarray(X)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
t = np.linspace(-1, 2, 50)
dirv = P1 - P0
line_pts = P0[None,:] + t[:,None] * dirv[None,:]
ax.plot(line_pts[:,0], line_pts[:,1], line_pts[:,2], label='Line', linewidth=2)
u = Q2 - Q1
v = Q3 - Q1
s = np.linspace( -0.5, 1.2, 10 )
r = np.linspace( -0.5, 1.2, 10 )
S,R = np.meshgrid(s, r)
plane_pts = Q1[None,None,:] + S[:,:,None]*u[None,None,:] + R[:,:,None]*v[None,None,:]
ax.plot_surface(plane_pts[:,:,0], plane_pts[:,:,1], plane_pts[:,:,2], alpha=0.5)
ax.scatter(*P0, color='red', s=40, label='P0 (line)')
ax.scatter(*P1, color='red', s=40, label='P1 (line)')
ax.scatter(*Q1, color='green', s=40, label='Q1 (plane)')
ax.scatter(*Q2, color='green', s=40, label='Q2 (plane)')
ax.scatter(*Q3, color='green', s=40, label='Q3 (plane)')
ax.scatter(*X,  color='black', s=70, label='Intersection')

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.legend()
plt.savefig("../figs/plot.png")
plt.show()

