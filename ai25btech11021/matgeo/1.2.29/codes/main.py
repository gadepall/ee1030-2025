import matplotlib.pyplot as plt
import numpy as np

W = np.array([50.91, 50.91])
V = np.array([0, 51])
R = W - V

origin = np.array([[0, 0], [0, 0]])

plt.figure(figsize=(8, 8))
plt.quiver(*origin, 
           [W[0], V[0], R[0]], 
           [W[1], V[1], R[1]],
           angles='xy', scale_units='xy', scale=1,
           color=['blue', 'green', 'red'],
           label=['Wind Vector ($\\vec{W}$)', 'Boat Vector ($\\vec{V}$)', 'Relative Wind ($\\vec{R}$)'])

plt.xlim(-10, 80)
plt.ylim(-10, 80)
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title("Vector Plot: Wind, Boat, and Relative Wind")
plt.xlabel("East-West Direction")
plt.ylabel("North-South Direction")

plt.savefig("vector_plot.png", dpi=300)
plt.show()
