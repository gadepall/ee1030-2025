import numpy as np
import matplotlib.pyplot as plt

k_value = 2.0
print(f"The value of k for which there is no solution is:")
print(f"  k = {k_value:.2f}")

x = np.linspace(-5, 5, 100)

y1 = 1 - 3 * x

y2 = (2 * k_value + 1 - (2 * k_value - 1) * x) / (k_value - 1)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$3x + y = 1$')
plt.plot(x, y2, label=f'${{{(2*k_value-1):.0f}}}x + {{{(k_value-1):.0f}}}y = {{{(2*k_value+1):.0f}}}$ (for k={k_value:.0f})', linestyle='--')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'Lines for k = {k_value:.2f} (No Solution)', fontsize=14)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()


