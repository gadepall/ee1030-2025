import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/') 
from call import load_vectors_from_c
 
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
a, b, c, v = load_vectors_from_c()
 
vectors = [a, b, c, v]
colors = ['r', 'g', 'b', 'orange']
labels = ['a', 'b', 'c', 'v']
def format_original_label(name, vec):
    x, y, z = int(vec[0]), int(vec[1]), int(vec[2])
    y_part = f"+ {y}ĵ" if y >= 0 else f"- {abs(y)}ĵ"
    z_part = f"+ {z}k̂" if z >= 0 else f"- {abs(z)}k̂"
    return f'${name}$ = {x}î {y_part} {z_part}'

# 3. Set up the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
origin = [0, 0, 0]

for vec, color, name in zip(vectors, colors, labels):
    legend_label = format_original_label(name, vec)
    ax.quiver(*origin, *vec, color=color,arrow_length_ratio=0.1, label=legend_label)
    # Add text label
    ax.text(*(vec * 1.1), f'${name}$', color=color, fontsize=15)
x_plane = np.linspace(-5, 5, 10)
y_plane = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x_plane, y_plane)
Z = X
ax.plot_surface(X, Y, Z, alpha=0.2, color='gray')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Finding a vector that is in the plane of vectors a and b')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.view_init(elev=25, azim=45)
ax.legend()
ax.grid(True)

plt.show()
# Save the final figure to a file
plt.savefig('fig.png')
