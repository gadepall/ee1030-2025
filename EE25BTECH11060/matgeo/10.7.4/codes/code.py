import numpy as np
import matplotlib.pyplot as plt
# Line: y = 2x + 2√3
def line(x):
    return 2*x + 2*np.sqrt(3)
# Parabola: y^2 = 16√3 x => x = y^2 / (16√3)
y_parabola = np.linspace(-10, 10, 400)
x_parabola = y_parabola**2 / (16 * np.sqrt(3))
# Ellipse: 2x^2 + y^2 = 4
theta = np.linspace(0, 2*np.pi, 400)
a = np.sqrt(2)  # semi-major axis
b = 2          # semi-minor axis
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)
# Line domain (chosen to cover range of ellipse and parabola)
x_line = np.linspace(-2, 2, 400)
y_line = line(x_line)

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(x_parabola, y_parabola, label=r'$y^2 = 16\sqrt{3}x$', color='green')
plt.plot(x_parabola, -y_parabola, color='green')  # the other half of the parabola
plt.plot(x_ellipse, y_ellipse, label=r'$2x^2 + y^2 = 4$', color='blue')
plt.plot(x_line, y_line, label=r'$y = 2x + 2\sqrt{3}$', color='red', linestyle='--')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title("Common Tangent to a Parabola and an Ellipse")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis('equal')
plt.show()
