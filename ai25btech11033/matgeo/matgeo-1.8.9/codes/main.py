import numpy as np

P = np.array([-6, 8])
O = np.array([0, 0])

distance = np.linalg.norm(P - O)
print(f"Distance from origin = {distance}")
