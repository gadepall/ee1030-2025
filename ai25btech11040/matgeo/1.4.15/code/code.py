import matplotlib.pyplot as plt
import numpy as np

p = np.array([7, -6])
q = np.array([3, 4])

l = 1
m = 2

r = (p*m + q*l)/(l+m)

points = [p, q, r]
x = [a[0] for a in points]
y = [a[1] for a in points]

if (r[0] > 0 and r[1] > 0):
    print("Q1")
if (r[0] > 0 and r[1] < 0):
    print("Q4")
if (r[0] < 0 and r[1] > 0):
    print("Q2")
if (r[0] < 0 and r[1] < 0):
    print("Q3")

fig, ax = plt.subplots()

fig.subplots_adjust(left=0.15, right=0.85)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Plotting P, Q and R')

ax.plot(x, y, 'b-')
ax.plot(x, y, 'ro')
ax.grid()

ax.annotate(f'P ({p[0]:.2f}, {p[1]:.2f})', p)
ax.annotate(f'Q ({q[0]:.2f}, {q[1]:.2f})', q)
ax.annotate(f'R ({r[0]:.2f}, {r[1]:.2f})', r)
fig.savefig('figs/plot.png')