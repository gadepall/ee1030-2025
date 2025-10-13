import numpy as np
import matplotlib.pyplot as plt

# Define theta range
theta = np.linspace(0, 2*np.pi, 500)

# Define beta function
beta = -( (np.sin(2*theta)/2)**4 ) - ( (np.sin(2*theta)/2)**2 ) - 2

# Minimum at theta = pi/4
theta_min = np.pi/4
beta_min = -( (np.sin(2*theta_min)/2)**4 ) - ( (np.sin(2*theta_min)/2)**2 ) - 2

# Plot
plt.figure(figsize=(8,5))
plt.plot(theta, beta, label=r'$\beta(\theta) = -\left(\frac{\sin(2\theta)}{2}\right)^4 - \left(\frac{\sin(2\theta)}{2}\right)^2 - 2$')

# Highlight minimum point
plt.scatter(theta_min, beta_min, color='red', zorder=5, label=r'Minimum at $\theta=\pi/4$')
plt.text(theta_min+0.2, beta_min-0.1, 
         rf'($\pi/4$, {beta_min:.2f})', color='red')

# Format x-axis in terms of pi
xticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4, 2*np.pi]
xtick_labels = [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$', 
                r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$']
plt.xticks(xticks, xtick_labels)

# Axis labels and legend
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\beta(\theta)$')
plt.title(r'Plot of $\beta(\theta)$ (0 to $2\pi$)')
plt.legend()
plt.grid(True)
plt.savefig('beta.png')
plt.show()

