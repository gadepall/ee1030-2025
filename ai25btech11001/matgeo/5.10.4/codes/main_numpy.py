import numpy as np
import numpy.linalg as LA
from sympy import *

m = Matrix([[1, 0, -1, 0],[2,0,0,-1],[0,2,0,-1],[0,1,-1,0]])
print(m.rref())
