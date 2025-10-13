import numpy as np
import numpy.linalg as LA
#import mpmath as mp
#from line.params import *
#from params import *

omat=np.array(([0,1],[-1,0]))
e1 = np.array(([1,0]))
e2 = np.array(([0,1]))
#Intersection of two lines
def line_isect(n1,c1,n2,c2):
  N=np.block([n1,n2]).T
  p = np.zeros((2,1))
  p[0] = c1
  p[1] = c2
  #Intersection
  P=np.linalg.solve(N,p)
  return P

def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

def line_norm(n,c,k1,k2):
    c = c/LA.norm(n)
    n = n/LA.norm(n)
    if c==0:
        A = np.zeros((2,1))
    elif np.array_equal(n, e1):
        A = np.array(([c, 0])).reshape(-1,1) 
    elif np.array_equal(n, e2):
        A = np.array(([0, c])).reshape(-1,1) 
    else:
        A = np.array(([c/n[0][0], 0])).reshape(-1,1) 
    m = omat@n
    return line_dir_pt(m,A,k1,k2)
