import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Direction cosine values
k1 = 1 / np.sqrt(3)
k2 = -k1

print("Possible values: k =", k1, "or", k2)

# Vectors for plotting
vec_pos = np.array([k1, k1, k1])
vec_neg = np.array([k2, k2, k2])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
origin = np.array([0,0,0])

# Plot both vectors
ax.quiver(*origin, *vec_pos, color='g', arrow_length_ratio=0.1,
          label=f"(k,k,k), k={k1:.3f}")
ax.quiver(*origin, *vec_neg, color='r', arrow_length_ratio=0.1,
          label=f"(-k,-k,-k), k={k1:.3f}")

# Axes limits
ax.set_xlim([-0.7,0.7])
ax.set_ylim([-0.7,0.7])
ax.set_zlim([-0.7,0.7])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Direction Cosine Vectors")
ax.legend()

plt.savefig("dir_cosines_both.png")
plt.show()

