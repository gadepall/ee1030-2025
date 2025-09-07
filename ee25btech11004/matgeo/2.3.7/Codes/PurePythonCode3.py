import numpy as np

import matplotlib.pyplot as plt

import sys

import numpy.linalg as LA

import math

vec1 = np.array([1,-2,-2])
vec2 = np.array([3,-6,2])

dot_product = vec1@vec2

norm1 = np.linalg.norm(vec1)
norm2 = np.linalg.norm(vec2)

cos = dot_product/(norm1*norm2)

angle = math.asin(cos)

print(angle*180/3.1415)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)

X, Y = np.meshgrid(x, y)

Z = (X-2*Y- 1)/2
z1 = (6*Y - 3*X)/2

ax.plot_surface(X, Y, Z, alpha=1, cmap='Blues')
ax.plot_surface(X, Y, z1, alpha=1, cmap='Oranges')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Plot of the planes')

plt.show()
