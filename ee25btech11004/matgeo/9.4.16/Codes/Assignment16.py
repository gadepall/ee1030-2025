import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,15,100)

y = 2*x*x - 7*x + 3

zero = np.zeros(100)

fig = plt.figure(figsize = (6,6))

ax = fig.add_subplot(111)

plt.plot(x,y, label='$2x^2 - 7x + 3$')
ax.scatter(3,0, label='(3,0)',color='green')
ax.scatter(0.5,0, label = '(0.5,0)', color = 'red')
plt.plot(x,zero)

plt.legend()
plt.grid(True)
plt.show()

