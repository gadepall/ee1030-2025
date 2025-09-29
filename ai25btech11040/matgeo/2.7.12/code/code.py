import matplotlib.pyplot as plt
import numpy as np
import ctypes

lib = ctypes.CDLL('./code.so')
lib.area.argtypes = [ctypes.c_double]*6
lib.area.restype = ctypes.c_double

a = np.array([0, -1])
b = np.array([2, 1])
c = np.array([0, 3])

d = (a + b)/2
e = (b + c)/2
f = (c + a)/2

area = 1/2 * np.abs(np.cross(d - e, d - f))

fig, ax = plt.subplots()

ax.plot(*a, 'ro')
ax.plot(*b, 'ro')
ax.plot(*c, 'ro')

ax.plot(*zip(a, b), 'r-')
ax.plot(*zip(b, c), 'r-')
ax.plot(*zip(c, a), 'r-')

ax.plot(*d, 'bo')
ax.plot(*e, 'bo')
ax.plot(*f, 'bo')

ax.plot(*zip(d, e), 'b-')
ax.plot(*zip(e, f), 'b-')
ax.plot(*zip(f, d), 'b-')

ax.annotate(f'A({a[0]}, {a[1]})', a, textcoords="offset points", xytext=(0,-10), ha='center', color='red')
ax.annotate(f'B({b[0]}, {b[1]})', b, textcoords="offset points", xytext=(10,0), ha='center', color='red')
ax.annotate(f'C({c[0]}, {c[1]})', c, textcoords="offset points", xytext=(0,10), ha='center', color='red')
ax.annotate(f'D({d[0]}, {d[1]})', d, textcoords="offset points", xytext=(10,0), ha='center', color='blue')
ax.annotate(f'E({e[0]}, {e[1]})', e, textcoords="offset points", xytext=(10,0), ha='center', color='blue')
ax.annotate(f'F({f[0]}, {f[1]})', f, textcoords="offset points", xytext=(10,0), ha='center', color='blue')

area = lib.area(d[0], d[1], e[0], e[1], f[0], f[1])
print(f'Area of triangle DEF = {area}')

plt.show()
fig.savefig('../figs/triangle_diagram.png')