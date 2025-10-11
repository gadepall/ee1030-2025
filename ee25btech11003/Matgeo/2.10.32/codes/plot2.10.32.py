import numpy as np
import matplotlib.pyplot as plt

# Condition: 9p^2 = 4q^2 => q = (3/2)p
p = 6
q = 9  # satisfies 9*36 = 4*81

# Define points
O = np.array([0, 0])
P = np.array([p, 0])
Q = np.array([0, q])

# R divides PQ internally in ratio 2:3
R = (3*P + 2*Q) / 5

# S divides PQ externally in ratio 2:3
S = (3*P - 2*Q) / (3 - 2)   # formula for external division

# Plot points
points = {'O':O, 'P':P, 'Q':Q, 'R':R, 'S':S}

plt.figure(figsize=(6,6))
for name, pt in points.items():
    plt.scatter(pt[0], pt[1], label=name)
    plt.text(pt[0]+0.2, pt[1]+0.2, name, fontsize=12)

# Draw lines PQ, OR, OS
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k--', label='PQ')
plt.plot([O[0], R[0]], [O[1], R[1]], 'r', label='OR')
plt.plot([O[0], S[0]], [O[1], S[1]], 'b', label='OS')

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Vectors OR and OS with OR ⟂ OS")
plt.show()

