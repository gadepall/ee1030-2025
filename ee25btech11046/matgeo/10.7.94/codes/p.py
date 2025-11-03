import numpy as np
import matplotlib.pyplot as plt

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ + O)
	return x_circ

center_fixed = np.array([0, 3]).reshape(-1, 1)
radius_fixed = 2.0

x_locus = np.linspace(-10, 10, 200)
y_locus = (x_locus**2 + 5) / 10

x_sample_center = 4.0
y_sample_center = (x_sample_center**2 + 5) / 10
center_sample = np.array([x_sample_center, y_sample_center]).reshape(-1, 1)
radius_sample = y_sample_center

fixed_circle_points = circ_gen(center_fixed, radius_fixed)
sample_circle_points = circ_gen(center_sample, radius_sample)

plt.figure(figsize=(10, 10))

plt.plot(x_locus, y_locus, 'r-', lw=2, label='Locus: $x^2 - 10y + 5 = 0$')
plt.plot(fixed_circle_points[0, :], fixed_circle_points[1, :], 'b-', label='Given Circle: $x^2 + (y-3)^2 = 4$')
plt.plot(sample_circle_points[0, :], sample_circle_points[1, :], 'g--', label='Example')
plt.scatter(center_fixed[0], center_fixed[1], color='blue', s=50, zorder=5)
plt.text(center_fixed[0]+0.2, center_fixed[1], 'C (3, 0)')
plt.scatter(center_sample[0], center_sample[1], color='green', s=50, zorder=5)
plt.text(center_sample[0]+0.2, center_sample[1], r'     $C_S$')

plt.title('Locus of the Center of  Circle')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.axhline()
plt.axvline()
plt.legend(loc='upper right')
plt.savefig("../figs/plot_p.jpg")
plt.show()
