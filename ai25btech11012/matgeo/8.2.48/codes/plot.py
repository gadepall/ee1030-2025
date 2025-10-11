import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/unnathi/Documents/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

def affine_transform(P,c,x):
    return P@x + c

# --- Parameters for parabola (from derivation) ---
V = np.array([[4,2],[2,1]])
u = np.array([2,16])
f = 16

# Eigen decomposition
lamda, P = LA.eigh(V)
if lamda[1] == 0:
    lamda = np.flip(lamda)
    P = np.flip(P, axis=1)

eta = u @ P[:,0]

# Vertex (center)
a = np.vstack((u.T + eta*P[:,0].T, V))
b = np.hstack((-f, eta*P[:,0]-u))
center = LA.lstsq(a,b,rcond=None)[0]

# Generate parabola in standard form
num_points = 1000
p_y = np.linspace(-10,10,num_points)   # tighter window
a_parab = -2*eta/lamda[1]
p_x = (p_y**2)/a_parab
p_std = np.vstack((p_x,p_y)).T

# Transform to actual parabola
p = np.array([affine_transform(P,center,p_std[i,:]) for i in range(num_points)]).T

# --- Focus and directrix ---
F = np.array([-1,-2])   # focus
x_vals = np.linspace(-6,6,400)
y_vals = (x_vals + 3)/2  # directrix: x - 2y + 3 = 0

# --- Plot ---
plt.figure(figsize=(7,7))
plt.plot(p[0,:], p[1,:], 'b', linewidth=2, label="Parabola")
plt.plot(x_vals, y_vals, 'g--', linewidth=2, label="Directrix: $x - 2y + 3 = 0$")

# Mark focus and vertex
plt.scatter(F[0], F[1], color="red", s=60, zorder=5, label="Focus F(-1,-2)")
plt.scatter(center[0], center[1], color="orange", s=60, zorder=5, label="Vertex")

# Annotate points
plt.annotate("F(-1,-2)", (F[0], F[1]), textcoords="offset points", xytext=(-30,-10), fontsize=10, color="red")
plt.annotate("Vertex", (center[0], center[1]), textcoords="offset points", xytext=(10,10), fontsize=10, color="orange")

# Adjust view (zoom near parabola)
plt.xlim(-6,4)
plt.ylim(-6,6)

# Final touches
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Parabola with Focus and Directrix")
plt.grid(True)
plt.axis("equal")
plt.legend()



plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/8.2.48/figs/fig.png')
plt.show()

