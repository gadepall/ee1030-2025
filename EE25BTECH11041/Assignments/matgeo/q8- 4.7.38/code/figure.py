import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plane 1
x1 = np.linspace(-5,5,100)
y1 = np.linspace(-5,5,100)
X1, Y1 = np.meshgrid(x1,y1)
Z1 = (-X1 + 2*Y1 + 4) / 3

# Plane 2
x2 = np.linspace(-5,5,100)
y2 = np.linspace(-5,5,100)
X2, Y2 = np.meshgrid(x2,y2)
Z2 = -Y2 + 2*X2 - 5

# Plane 3 (required plane)
x3 = np.linspace(-5,5,100)
y3 = np.linspace(-5,5,100)
X3, Y3 = np.meshgrid(x3,y3)
Z3 = (X3 + Y3 - 1) / 4

# Plot surfaces
ax.plot_surface(X1, Y1, Z1, alpha=0.5, color='red')
ax.plot_surface(X2, Y2, Z2, alpha=0.5, color='blue')
ax.plot_surface(X3, Y3, Z3, alpha=0.5, color='green')

# Legend proxies (like in main.py)
plane_proxy = [plt.Rectangle((0,0),1,1,fc=c) for c in ["red","blue","green"]]
ax.legend(plane_proxy, ["Plane 1", "Plane 2", "Required Plane"], loc="best")

# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Three Planes")

plt.savefig("Figure.png", dpi=200)
plt.show()

