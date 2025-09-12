import numpy as np
import matplotlib.pyplot as plt

def distance3D(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Points
A, B = (2,3,5), (4,3,1)
C, D = (-3,7,2), (2,4,-1)
E, F = (-1,3,-4), (1,-3,4)
G, H = (2,-1,3), (-2,1,3)

print("AB =", distance3D(A,B))
print("CD =", distance3D(C,D))
print("EF =", distance3D(E,F))
print("GH =", distance3D(G,H))

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

pairs = [(A,B,'r'),(C,D,'g'),(E,F,'b'),(G,H,'k')]
for P, Q, c in pairs:
    ax.plot([P[0],Q[0]], [P[1],Q[1]], [P[2],Q[2]], c+"-o")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Segments between given points")
plt.savefig("/home/user/Matrix/Matgeo_assignments/1.9.15/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()