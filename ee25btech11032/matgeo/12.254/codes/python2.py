import math
import numpy as np
import numpy.linalg as LA

a = -0.5 + 1j*np.sqrt(3)/2

v1 = np.array([1, 1, 1], dtype=complex)
v2 = np.array([1, a, a**2], dtype=complex)

ans = np.dot(v1, v2)
ans = np.round(ans, 10)

print("Orthogonal : ", ans)
