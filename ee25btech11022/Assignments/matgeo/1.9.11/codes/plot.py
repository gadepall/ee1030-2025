import matplotlib.pyplot as plt
import numpy as np
from call import get_points

k, pt1, pt2 = get_points()

plt.figure(figsize=(7,5))
plt.scatter(pt1[0], pt1[1], color='red', label=f'First point ({pt1[0]:.2f}, {pt1[1]:.2f})')
plt.scatter(pt2[0], pt2[1], color='green', label=f'Second point ({pt2[0]:.2f}, {pt2[1]:.2f})')
plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], 'b--', label='Segment')
plt.title(f'Points with positive k: {k:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()

