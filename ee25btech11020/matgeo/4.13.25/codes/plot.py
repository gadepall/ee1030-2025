import numpy as np
import matplotlib.pyplot as plt

VA = np.array([1, 2])
VC = np.array([-3, -6])
V  = np.array([0.33, -2.67])
VB = np.array([-2.33, -1.33])
O  = np.array([-1, -2])

points = np.array([VA, V, VC, VB, VA])

plt.figure(figsize=(6,6))
plt.plot(points[:,0], points[:,1], 'b-', linewidth=2)

for P, name in zip([VA, V, VC, VB, O], ["A","V","C","B","O"]):
    plt.scatter(P[0], P[1], color="red")
    label = f"{name}{tuple(P)}"
    plt.text(P[0]+0.2, P[1]+0.2, label, fontsize=11)

plt.axis("equal")
plt.grid(True)
plt.title("Rhombus with Coordinates")
plt.savefig("../figs/img2.png")

