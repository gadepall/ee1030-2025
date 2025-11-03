import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL('./2.10.78.so')

# Set argument and return types
lib.matvec2x2.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,2)),
                          np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
                          np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,))]

lib.matvec3x3.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, shape=(3,3)),
                          np.ctypeslib.ndpointer(dtype=np.float64, shape=(3,)),
                          np.ctypeslib.ndpointer(dtype=np.float64, shape=(3,))]

# Initial point
P = np.array([4.0, 1.0])

# Step 1: Reflection over y = x → swap x and y
reflect_mat = np.array([[0.0, 1.0],
                        [1.0, 0.0]])
P1 = np.zeros(2)
lib.matvec2x2(reflect_mat, P, P1)

# Step 2: Translation +2 in x-direction using 3x3 matrix
P1_h = np.array([P1[0], P1[1], 1.0])
translate_mat = np.array([[1.0, 0.0, 2.0],
                          [0.0, 1.0, 0.0],
                          [0.0, 0.0, 1.0]])
P2_h = np.zeros(3)
lib.matvec3x3(translate_mat, P1_h, P2_h)
P2 = P2_h[:2]

# Step 3: Rotation by pi/4 (45° counterclockwise)
theta = np.pi / 4
cos_t = np.cos(theta)
sin_t = np.sin(theta)
rotation_mat = np.array([[cos_t, -sin_t],
                         [sin_t, cos_t]])
P3 = np.zeros(2)
lib.matvec2x2(rotation_mat, P2, P3)

# Plotting the transformation steps
points = np.array([P, P1, P2, P3])
labels = ['Original (4,1)', 'After Reflection', 'After Translation', 'After Rotation (Final)']
colors = ['blue', 'orange', 'green', 'red']

plt.figure(figsize=(8, 8))
for i, point in enumerate(points):
    plt.plot(point[0], point[1], 'o', label=labels[i], color=colors[i])
    plt.text(point[0]+0.1, point[1]+0.1, f'{labels[i]}')

plt.plot(points[:,0], points[:,1], '--k', alpha=0.5)
plt.grid(True)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.legend()
plt.title("Transformation of Point (4,1)")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.show()

# Final result
print(f"Final coordinates after all transformations: ({P3[0]}, {P3[1]})")

