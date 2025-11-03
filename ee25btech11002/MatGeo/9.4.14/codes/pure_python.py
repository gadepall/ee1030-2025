import numpy as np
import matplotlib.pyplot as plt

def function(x):
  return x**2 - 12*x + 3;

x = np.linspace(-3, 15, 100)
y = function(x)
y1 = np.zeros(100)
def quadratic(a, b, c):
  d = b**2 - 4*a*c
  x1 = (-b + np.sqrt(d)) / (2*a)
  x2 = (-b - np.sqrt(d)) / (2*a)
  return x1, x2

x1, x2 = quadratic(1, -12, 3)
fig, ax = plt.subplots()
ax.plot(x, y, label='x^2 - 12x + 3') 
ax.plot(x, y1, label='y = 0') 
ax.scatter(x1, 0, color="black", label=f'Root 1 ({x1:.2f}, 0)') 
ax.text(x1, 0, f'({x1:.2f}, 0)')
ax.scatter(x2, 0, color="black", label=f'Root 2 ({x2:.2f}, 0)') 
ax.text(x2, 0, f'({x2:.2f}, 0)')
ax.grid(True)
ax.legend()
ax.legend(loc="lower right")
plt.show()