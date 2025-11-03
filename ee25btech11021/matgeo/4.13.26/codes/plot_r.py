import numpy as np
import matplotlib.pyplot as plt

# Load computed R points
R_points = np.load("R_points.npy")

# Remove any points with extremely large values (slope ~ 0)
mask = (np.abs(R_points[:,0]) < 1000) & (np.abs(R_points[:,1]) < 1000)
R_points = R_points[mask]

# Plot the locus of R
plt.figure(figsize=(8,6))
plt.plot(R_points[:,0], R_points[:,1], color='red', linewidth=2)
plt.title("Locus of R for rectangle OPRQ")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()

