import numpy as np
import matplotlib.pyplot as plt

T = np.array([
    [0.5,  0,    0],
    [0,    0.25, 0],
    [1,    2,    1]
])

P_homogeneous = np.array([1, 1, 1])

P_t = P_homogeneous @ T

P_original = P_homogeneous[:2]
P_transformed = P_t[:2]

plt.figure(figsize=(8, 8))
origin = [0, 0]

plt.plot([origin[0], P_original[0]], [origin[1], P_original[1]], 
          color='blue', label='Original Vector P')

plt.plot([origin[0], P_transformed[0]], [origin[1], P_transformed[1]], 
          color='red', label="Transformed Vector P'")
          
plt.scatter(origin[0], origin[1], s=100, color='black', zorder=5)
plt.scatter(P_original[0], P_original[1], s=100, color='blue', zorder=5)
plt.scatter(P_transformed[0], P_transformed[1], s=100, color='red', zorder=5)

plt.text(P_original[0] - 0.4, P_original[1], f'         P({P_original[0]}, {P_original[1]})', fontsize=12)
plt.text(P_transformed[0] + 0.1, P_transformed[1], f"P'({P_transformed[0]}, {P_transformed[1]})", fontsize=12)
plt.text(origin[0], origin[1], '    O (0, 0)', fontsize=12)


plt.title("2D CAD Transformation")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(-0.2,2.5)
plt.axhline(color='grey')
plt.axvline(color='grey')
plt.grid()
plt.savefig("../figs/plot_p.jpg")
plt.show()
