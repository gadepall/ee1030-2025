import numpy as np

# Orthogonal matrix for 90-degree rotation
omat = np.array([[0, 1], [-1, 0]])

# 2x2 Identity matrix
I = np.eye(2)

# Standard basis vectors
e1 = I[:, [0]]
e2 = I[:, [1]]
