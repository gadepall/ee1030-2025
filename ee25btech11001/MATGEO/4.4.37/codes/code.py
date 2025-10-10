# code.py
import numpy as np
import matplotlib.pyplot as plt

# Compute m vector directly
m = np.array([1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3)])
print("m vector from Python:", m)

# Point through which line passes
P = np.array([2, 3, -5])

# Line: r = P + t*m
t = np.linspace(-10, 10, 100)
X = P[0] + t * m[0]
Y = P[1] + t * m[1]
Z = P[2] + t * m[2]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z, label="Line through (2,3,-5)")
ax.scatter(P[0], P[1], P[2], color="red", label="Point (2,3,-5)")
ax.legend()
plt.show()

