import numpy as np
import matplotlib.pyplot as plt

# Generalized dot product
def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have same length")
    return sum(a[i]*b[i] for i in range(len(a)))

# Check orthogonality
def is_orthogonal(a, b):
    return dot_product(a, b) == 0

# Normal and direction vectors for a 2D line Ax + By = C
def normal_vector(A, B):
    return np.array([A, B])

def direction_vector(A, B):
    return np.array([B, -A])

# Example: x = 3y => 1*x - 3*y = 0
A, B = 1, -3
nvec = normal_vector(A, B)
dvec = direction_vector(A, B)

print("Normal vector:", nvec)
print("Direction vector:", dvec)
print("Orthogonal check:", is_orthogonal(nvec, dvec))

# Plotting
origin = np.array([[0,0]])
plt.quiver(*origin.T, nvec[0], nvec[1], color='r', scale=1, scale_units='xy', angles='xy', label='Normal')
plt.quiver(*origin.T, dvec[0], dvec[1], color='b', scale=1, scale_units='xy', angles='xy', label='Direction')

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.title('Direction and Normal Vectors for x = 3y')
plt.show()
