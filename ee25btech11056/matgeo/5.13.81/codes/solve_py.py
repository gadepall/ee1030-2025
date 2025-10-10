import numpy as np 

count = 0

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    k1 = a - d 
                    k2 = d - e 
                    A = np.array([[0,1,c],[0,k1,k2],[1,b,e]])
                    det = np.linalg.det(A) 
                    if det==1 or det==-1 :
                       count+=1 



print("The number of possible arrays is:",count)



