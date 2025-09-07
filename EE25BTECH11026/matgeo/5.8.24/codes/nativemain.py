import numpy as np
A=np.array([[1,-1,0,0],[-2,0,1,0],[0,1,0,-2],[0,0,1,-1]])
b=np.array([3,0,0,30])
x=np.linalg.solve(A ,b)
print(f"Ani's age:{x[0]:.0f} years")
print(f"Bijoya's age:{x[1]:.0f} years")
