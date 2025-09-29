import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load shared object
lib = ctypes.CDLL("./points.so")
lib.compute_k.restype = ctypes.c_double

# Call C function to get positive k
k_pos = lib.compute_k()
k_neg = -k_pos

print("Possible values of k from C: k =", k_pos, "or", k_neg)

# Vectors for plotting
vec_pos = np.array([k_pos, k_pos, k_pos])
vec_neg = np.array([k_neg, k_neg, k_neg])

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
origin = np.array([0,0,0])

# Plot both vectors
ax.quiver(*origin, *vec_pos, color='r', arrow_length_ratio=0.1,
          label=f"(k,k,k), k={k_pos:.3f}")
ax.quiver(*origin, *vec_neg, color='b', arrow_length_ratio=0.1,
          label=f"(-k,-k,-k), k={k_pos:.3f}")

# Axes limits
ax.set_xlim([-0.7,0.7])
ax.set_ylim([-0.7,0.7])
ax.set_zlim([-0.7,0.7])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Direction Cosine Vectors from C")
ax.legend()

plt.savefig("dir_cosines_c_both.png")
plt.show()

