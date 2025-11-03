import numpy as np
2 import matplotlib.pyplot as plt
3 from mpl_toolkits.mplot3d import Axes3D
4
5 # Direction ratios
6 a, b, c = -18, 12, -4
7
8 # Normalize to get direction cosines
9 magnitude = np.sqrt(a**2 + b**2 + c**2)
0 alpha, beta, gamma = a/magnitude, b/magnitude, c/magnitude
1
2 # Create figure
3 fig = plt.figure()
4 ax = fig.add_subplot(111, projection='3d')
5
6 # Plot axes
7 ax.quiver(0, 0, 0, 1, 0, 0, color='blue', label='x-axis')
8 ax.quiver(0, 0, 0, 0, 1, 0, color='red', label='y-axis')
9 ax.quiver(0, 0, 0, 0, 0, 1, color='green', label='z-axis')
# Plot direction vector
2 ax.quiver(0, 0, 0, alpha, beta, gamma, color='skyblue', label='
Direction Vector')
3 # Annotate direction cosines
4 ax.text(alpha, beta, gamma, f'({alpha:.3f}, {beta:.3f}, {gamma:.3
f})', fontsize=10)
5 ax.text2D(0.05, 0.95, f'Direction Cosines:\n = {alpha:.3f}\n = {
beta:.3f}\n = {gamma:.3f}', transform=ax.transAxes)
6 # Set limits and labels
7 ax.setxlim([-1, 1])
8 ax.setylim([-1, 1])
9 ax.setzlim([-1, 1])
0 ax.setxlabel('X')
1 ax.setylabel('Y')
2 ax.setzlabel('Z')
3 ax.settitle('Direction Cosines of a Line')
4 plt.legend()
5 plt.tightlayout()
6 plt.show()
