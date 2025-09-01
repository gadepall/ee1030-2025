import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/') 
from call import load_vectors_from_c
 
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
a, b, c, v = load_vectors_from_c()
 
vx, vy, vz = v[0], v[1], v[2]
j_part_str = f"+ {vy}ĵ" if vy >= 0 else f"- {abs(vy)}ĵ"
k_part_str = f"+ {vz}k̂" if vz >= 0 else f"- {abs(vz)}k̂"
print(f"The vector in the plane of a and b is: {vx}î {j_part_str} {k_part_str}")

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
origin = [0, 0, 0]

# Plot vectors
vectors = {'a': (a, 'r'), 'b': (b, 'g'), 'c': (c, 'b'), 'v': (v, 'orange')}
for name, (vec, color) in vectors.items():
    x, y, z = int(vec[0]), int(vec[1]), int(vec[2])
    j_part = f"+ {y}ĵ" if y >= 0 else f"- {abs(y)}ĵ"
    k_part = f"+ {z}k̂" if z >= 0 else f"- {abs(z)}k̂"
    label_text = f'${name}$ = {x}î {j_part} {k_part}'
    ax.quiver(origin[0], origin[1], origin[2], vec[0], vec[1], vec[2],
              color=color, label=label_text,
              arrow_length_ratio=0.1, linewidth=2)
    ax.text(vec[0]*1.1, vec[1]*1.1, vec[2]*1.1, f'${name}$', color=color, fontsize=15)

# Plot the plane
x_plane = np.linspace(-5, 5, 10); y_plane = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x_plane, y_plane)
Z = X
ax.plot_surface(X, Y, Z, alpha=0.2, color='gray')
 
ax.view_init(elev=25, azim=45)
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title('Finding a vector that is in the plane of vectors a and b')
ax.legend()
ax.grid(True)
ax.set_xlim([-5, 5]); ax.set_ylim([-5, 5]); ax.set_zlim([-5, 5])

plt.show()

# Save the final figure to a file
plt.savefig('fig.png')