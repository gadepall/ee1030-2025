import numpy as np
import matplotlib.pyplot as plt

# Side lengths
AB = 5
BC = 6
CA = 7

# Place A at (0,0), B at (5,0)
A = (0, 0)
B = (AB, 0)

# Calculate cosA using Law of Cosines
cosA = (AB**2 + CA**2 - BC**2) / (2 * AB * CA)
sinA = np.sqrt(1 - cosA**2)

# Coordinates of C
Cx = CA * cosA
Cy = CA * sinA
C = (Cx, Cy)

print('Coordinates of A:', A)
print('Coordinates of B:', B)
print('Coordinates of C:', (round(Cx, 2), round(Cy, 2)))

# 2D graph
plt.figure(figsize=(7,7))
plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-', label='AB (5 cm)')
plt.plot([B[0], C[0]], [B[1], C[1]], 'go-', label='BC (6 cm)')
plt.plot([C[0], A[0]], [C[1], A[1]], 'ro-', label='CA (7 cm)')

for point, label in zip([A, B, C], ['A', 'B', 'C']):
    plt.text(point[0], point[1], label, fontsize=14, fontweight='bold', ha='right', color='black')

plt.xlabel('X (cm)')
plt.ylabel('Y (cm)')
plt.title('Triangle with sides 5 cm, 6 cm, 7 cm')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.tight_layout()
plt.savefig('triangle_5_6_7.png', dpi=200)
plt.close()

