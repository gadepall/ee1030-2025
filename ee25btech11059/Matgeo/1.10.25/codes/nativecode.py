import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the line with direction cosines
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
z = np.linspace(-3, 3, 100)

# Direction cosines for the line (example: cosines of 30°, 60°)
cos_30 = np.cos(np.radians(30))
cos_60 = np.cos(np.radians(60))

# Parametric equations for the line with direction cosines
x_line = x * cos_30
y_line = y * cos_60
z_line = z

# Plot the line
ax.plot(x_line, y_line, z_line, label='Line with direction cosin_
