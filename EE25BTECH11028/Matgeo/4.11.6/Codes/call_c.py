import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


lib = ctypes.CDLL("./libplane.so")

# Variables to store plane coefficients
a = ctypes.c_double()
b = ctypes.c_double()
c = ctypes.c_double()
d = ctypes.c_double()

# Call the C function to get coefficients
lib.get_plane(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c), ctypes.byref(d))

# Extract values
a, b, c, d = a.value, b.value, c.value, d.value
print(f"Plane equation: {a}x + {b}y + {c}z + {d} = 0")


x = np.linspace(-5, 5, 30)   # X range
z = np.linspace(-5, 5, 30)   # Z range
X, Z = np.meshgrid(x, z)

# Solve plane eqn for Y:  y = (-ax - cz - d)/b
Y = (-a*X - c*Z - d) / b

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z, alpha=0.5, color="cyan", label="Plane")

ax.plot([-5, 5], [0, 0], [0, 0], color="red", linewidth=3, label="X-axis")

# Take a point on X-axis (0,0,0)
P = np.array([0,0,0])

# Formula: foot of perpendicular from point to plane
num = a*P[0] + b*P[1] + c*P[2] + d
den = a*a + b*b + c*c

Px = P[0] - a*num/den
Py = P[1] - b*num/den
Pz = P[2] - c*num/den

# Plot distance line
ax.plot([P[0], Px], [P[1], Py], [P[2], Pz],
        color="black", linewidth=3, label="Shortest distance")

# Mark points
ax.scatter(P[0], P[1], P[2], color="red", s=50, label="Origin (on X-axis)")
ax.scatter(Px, Py, Pz, color="blue", s=50, label="Foot on Plane")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Plane y - 3z + 6 = 0 and Distance from X-axis")
ax.legend()

plt.show()
\end{lstlisting}

\end{frame}
\end{document}

