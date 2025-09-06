import matplotlib.pyplot as plt
import numpy as np

# Unit vector a (choose direction, here along x-axis)
ax, ay = 1.0, 0.0

# From algebra: |x| = 3 (see previous solution for derivation)
mag_x = 3.0

# x vector
x = mag_x * np.array([ax, ay])

# Origin for plotting
O = np.array([0, 0])
a = np.array([ax, ay])

plt.figure(figsize=(6, 6))

# Plot vector a
plt.quiver(O[0], O[1], a[0], a[1], angles='xy', scale_units='xy', scale=1, color='green', label='a (unit)')
plt.text(a[0], a[1], f'a({a[0]:.1f}, {a[1]:.1f})', fontsize=10, ha='left', va='bottom')

# Plot vector x
plt.quiver(O[0], O[1], x[0], x[1], angles='xy', scale_units='xy', scale=1, color='blue', label='x = 3a')
plt.text(x[0], x[1], f'x({x[0]:.1f}, {x[1]:.1f})', fontsize=10, ha='left', va='bottom')

# Plot origin
plt.scatter(O[0], O[1], color='black', s=40)
plt.text(O[0], O[1], 'O(0,0)', fontsize=10, ha='left', va='top')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Solution to 2.8.8 using Native Python")
plt.legend()
plt.grid(True)
plt.xlim(-1, 4)
plt.ylim(-1, 2)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/2.8.8/figs/figure1.png")
plt.show()
