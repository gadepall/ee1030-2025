import numpy as np
import numpy.linalg as LA


a,d,a2,d2=0,2*5,8,4
b,c,b2=0,5*5,10
print(LA.matrix_rank(np.array([[a2-d2,a2,a2+d2],[b2-d2,b2,b2+d2],[a-b+c-d,a-b,a-b-c+d]])))
