import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, -2])

m = 7

unit_v = a/np.linalg.norm(a)

req_vec = m*unit_v

print(req_vec)

plt.plot([0, a[0]], [0, a[1]], label='Vector a', marker='o')
plt.plot([0, req_vec[0]], [0, req_vec[1]], label='Required Vector', marker='o')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.savefig('../figs/plot.png')
plt.show()