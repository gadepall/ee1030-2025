import numpy as np

a = np.array([1, -2])

m = 7

unit_v = a/np.linalg.norm(a)

req_vec = m*unit_v

print(req_vec)