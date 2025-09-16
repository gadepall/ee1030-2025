import numpy as np

A,B,C = np.array([-2,3]),np.array([8,3]),np.array([6,7])
a=B-C
b=A-C
c=A-B
print(f"Dot prodouct of a and b ={np.dot(a,b)}")
print(f"Dot prodouct of a and c ={np.dot(a,c)}")
print(f"Dot prodouct of b and c ={np.dot(b,c)}")



