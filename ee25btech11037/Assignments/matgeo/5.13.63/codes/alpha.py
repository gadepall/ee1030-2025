import numpy as np
import matplotlib.pyplot as plt

# Define theta range for one cycle
theta = np.linspace(0, 2*np.pi, 500)

# Define alpha function
alpha = 1 - (np.sin(2*theta)**2)/2

# Point of minimum at theta = pi/4
theta_min = np.pi/4
alpha_min = 1 - (np.sin(2*theta_min)**2)/2

# Plot
plt.figure(figsize=(8,5))
plt.plot(theta, alpha, label=r'$\alpha(\theta) = 1 - \frac{\sin^2(2\theta)}{2}$')

# Highlight minimum point
plt.scatter(theta_min, alpha_min, color='red', zorder=5, label=r'Minimum at $\theta=\pi/4$')
plt.text(theta_min+0.2, alpha_min-0.1, 
         rf'($\pi/4$, {alpha_min:.2f})', color='red')

# Format x-axis in terms of pi
xticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4, 2*np.pi]
xtick_labels = [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$', 
                r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$']
plt.xticks(xticks, xtick_labels)

# Axis labels and legend
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\alpha(\theta)$')
plt.title(r'Plot of $\alpha(\theta) = 1 - \frac{\sin^2(2\theta)}{2}$ (0 to $2\pi$)')
plt.legend()
plt.grid(True)
plt.savefig('alpha.png')
plt.show()

