import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6,6))

ax = plt.subplot(111)


ax.axhline(y=2, color='r', linestyle='-')

ax.set_ylim(0, 4)
ax.set_xlim(0, 10)

ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("Plot of the Equation y = 2")

ax.grid(True)

plt.show()
