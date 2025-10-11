import numpy as np
import matplotlib.pyplot as plt

# Ellipse: x^2/4 + y^2 = 1

a_e, b_e = 2, 1
h_e, k_e = 0, 0

theta = np.linspace(0, 2*np.pi, 400)
x_ellipse = h_e + a_e * np.cos(theta)
y_ellipse = k_e + b_e * np.sin(theta)

# Ellipse foci
c_e = np.sqrt(a_e**2 - b_e**2)
focus1 = (h_e + c_e, k_e)
focus2 = (h_e - c_e, k_e)

# Hyperbola: x^2/3 - y^2 = 1
a_h = np.sqrt(3)
b_h = 1
h_h, k_h = 0, 0

x_h = np.linspace(-5, 5, 2000)
x_h = x_h[np.abs(x_h) >= a_h]  # valid domain
y_h = np.sqrt((x_h**2 / a_h**2 - 1) * b_h**2)

# Hyperbola foci (±2, 0)
c_h = 2
focus_h1 = (h_h + c_h, k_h)
focus_h2 = (h_h - c_h, k_h)

# Check if hyperbola passes through ellipse focus
x_f, y_f = focus1
lhs = x_f**2 / a_h**2 - y_f**2 / b_h**2
print("Hyperbola LHS at ellipse focus =", lhs)

plt.plot(x_ellipse, y_ellipse, label=r'Ellipse: $\frac{x^2}{4} + y^2 = 1$')
plt.plot(x_h, y_h, 'r', label=r'Hyperbola: $\frac{x^2}{3} - y^2 = 1$')
plt.plot(x_h, -y_h, 'r')

# Ellipse foci
plt.scatter(*focus1, color='green', s=80, label='Ellipse Focus (+)')
plt.scatter(*focus2, color='green', s=80, label='Ellipse Focus (-)')

# Hyperbola foci
plt.scatter(*focus_h1, color='purple', s=80, label='Hyperbola Focus (+)')
plt.scatter(*focus_h2, color='purple', s=80, label='Hyperbola Focus (-)')

# Annotate foci
plt.text(focus1[0]+0.1, focus1[1]+0.1, f'({focus1[0]:.2f}, {focus1[1]:.2f})', fontsize=9)
plt.text(focus2[0]-0.8, focus2[1]+0.1, f'({focus2[0]:.2f}, {focus2[1]:.2f})', fontsize=9)
plt.text(focus_h1[0]+0.1, focus_h1[1]-0.3, f'({focus_h1[0]:.2f}, {focus_h1[1]:.2f})', fontsize=9)
plt.text(focus_h2[0]-0.9, focus_h2[1]-0.3, f'({focus_h2[0]:.2f}, {focus_h2[1]:.2f})', fontsize=9)

plt.gca().set_aspect('equal')
plt.legend(loc = "upper right", fontsize=8) 
plt.grid(True)
plt.title("Ellipse and Hyperbola with Reciprocal Eccentricities")
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/8.4.16/figs/Figure_1.png")
plt.show()
