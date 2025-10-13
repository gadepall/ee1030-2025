import numpy as np
import matplotlib.pyplot as plt

# Circle parameters
h, k = 1, -1
r = 5

# Line equations
x = np.linspace(-8, 8, 400)
y1 = (-2*x - 1)/3          # 2x + 3y + 1 = 0
y2 = 3*x - 4               # 3x - y - 4 = 0

# Circle
theta = np.linspace(0, 2*np.pi, 400)
xc = h + r * np.cos(theta)
yc = k + r * np.sin(theta)

# Plot setup
plt.figure(figsize=(7,7))
plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='green')
plt.plot(xc, yc, color='red')

# Centre
plt.scatter(h, k, color='black', s=50)
plt.text(h+0.2, k-0.5, 'C(1, -1)', fontsize=10)

# Annotate equations beside lines 
# For 2x + 3y + 1 = 0
plt.text(4, (-2*4 - 1)/3 + 0.5, r'$2x + 3y + 1 = 0$', color='blue', fontsize=10)

# For 3x - y - 4 = 0
plt.text(1.5, 3*(1.5) - 4 + 0.5, r'$3x - y - 4 = 0$', color='green', fontsize=10)

# Axes and styling
plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)
plt.gca().set_aspect('equal', adjustable='box')

plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circle and Diametral Lines')
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/7.4.17/figs/circle.png")
plt.show()
