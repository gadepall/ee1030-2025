#Code by GVV Sharma
#December 7, 2019
#Revised July 15, 2020
#released under GNU GPL
#Functions related to line
import numpy as np
import numpy.linalg as LA
import mpmath as mp
#from line.params import *
from params import *


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@dir_vec(A,B)
  #return np.matmul(omat, dir_vec(A,B))

def ang_vec(m1,m2):
    return np.arccos(float((m1.T@m2)/(np.linalg.norm(m1)*np.linalg.norm(m2))))
    #return mp.acos(float((m1.T@m2)/(np.linalg.norm(m1)*np.linalg.norm(m2))))

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generating line using parametric form
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#Normal to parametric
def norm_to_para(n,c,k1,k2):
    m = omat@n
    A = c*n/(LA.norm(n)**2)
    return line_dir_pt(m,A,k1,k2)

#Normal to parametric
def param_norm(n,c):
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
    return m,A

#Intersection of two lines
def line_isect(n1,c1,n2,c2):
  N=np.block([[n1.T],[n2.T]])
  C=np.array([c1,c2])
  return LA.solve(N,C)

# Added function to calculate a unit vector
def calculate_unit_vector(vector):
  """
  Calculates the magnitude and unit vector of a given vector.

  Args:
    vector: A numpy array representing the vector.

  Returns:
    A tuple containing:
      - The original vector (numpy array).
      - The magnitude of the vector (float).
      - The unit vector (numpy array).
  """
  magnitude = np.linalg.norm(vector)

  # Avoid division by zero for a zero vector
  if magnitude == 0:
      raise ValueError("Cannot calculate the unit vector of a zero vector.")

  unit_vector = vector / magnitude
  return vector, magnitude, unit_vector


