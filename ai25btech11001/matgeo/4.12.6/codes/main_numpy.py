import numpy as np
import numpy.linalg as LA

a = np.array([980,14]).reshape(-1,1)
b = np.array([1220,16]).reshape(-1,1)
c = np.array([1340,17]).reshape(-1,1)

m = np.block([[a-b,c-b]])

print(m)
print(LA.matrix_rank(m))
