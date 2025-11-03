import numpy as np
import numpy.linalg as LA

a = np.array([[2,3],[2,4]])
b = np.array([11,-24]).reshape(-1,1)
print(c:=LA.solve(a,b))

print((c[1]-3)/c[0] == -19/29)
