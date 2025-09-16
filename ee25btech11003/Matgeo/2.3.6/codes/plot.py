import numpy as np
import matplotlib.pyplot as plt
import os

#to save figure in the figs folder
figs_folder = os.path.join("..","figs")

# Given magnitude and angle
magnitude = 3
angle_deg = 60  # angle between the vectors in degrees
angle_rad = np.deg2rad(angle_deg)  # convert to radians

# Define vector a along the x-axis
a = np.array([magnitude, 0])

# Define vector b making 60 degrees with vector a
b = np.array([magnitude * np.cos(angle_rad), magnitude * np.sin(angle_rad)])

# Plotting
plt.figure(figsize=(6, 6))

# Plot vector a
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector a')

# Plot vector b
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector b')

# Settings for the plot
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Annotate vectors
plt.text(a[0] + 0.1, a[1] + 0.1, 'a', fontsize=12, color='blue')
plt.text(b[0] + 0.1, b[1] + 0.1, 'b', fontsize=12, color='red')

# Title and labels
plt.title("Two Vectors with Magnitude 3 and Angle 60° Between Them")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.savefig(os.path.join(figs_folder,"fig1.png"))
plt.show()

