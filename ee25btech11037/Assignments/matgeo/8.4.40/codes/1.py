import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 4
b = 2
r = 1

# Angle parameter
theta = np.linspace(0, 2*np.pi, 400)

# Original ellipse (center at origin)
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)

# Locus of R: shifted ellipse (centered at (r,0))
x_locus = r + a * np.cos(theta)
y_locus = b * np.sin(theta)

# Plotting
# Increased figure size slightly to make space for the legend
plt.figure(figsize=(8, 7)) 
ax = plt.subplot(111)

ax.plot(x_ellipse, y_ellipse, label=r'Original ellipse: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$')
ax.plot(x_locus, y_locus, label=r'Locus of R: $\frac{(x-r)^2}{a^2}+\frac{y^2}{b^2}=1$')

# Mark centers
ax.scatter(0, 0, color='black', marker='o', label='Center of ellipse (0,0)')
ax.scatter(r, 0, color='red', marker='x', s=80, label='Center of locus ellipse (r,0)')

ax.set_aspect('equal', 'box')
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Ellipse and Locus of R (a={a}, b={b}, r={r})")
plt.grid(True)

# *** MODIFIED LINE ***
# Move the legend outside of the plot area
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust layout to make sure legend fits
plt.tight_layout(rect=[0, 0, 0.9, 1]) # rect leaves space on the right

plt.savefig('1.png')
plt.show()
