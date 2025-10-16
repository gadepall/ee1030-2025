#Code by GVV Sharma
#December 7, 2019
#Revised July 15, 2020
#released under GNU GPL
#Functions related to line

import numpy as np
from .params import * # Imports omat, I, e1, e2

def dir_vec(A, B):
  """Calculates the direction vector from point A to point B."""
  return B - A

def norm_vec(A, B):
  """Calculates a vector normal to the line segment AB."""
  return omat @ dir_vec(A, B)

def line_gen(A, B):
  """Generates points for a line segment between two points."""
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim, len))
  lam_1 = np.linspace(0, 1, len)
  for i in range(len):
    temp1 = A + lam_1[i] * (B - A)
    x_AB[:, i] = temp1.T
  return x_AB

def line_dir_pt(m, A, k1, k2):
  """Generates points for a line given a direction vector and a point."""
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim, len))
  lam_1 = np.linspace(k1, k2, len)
  for i in range(len):
    temp1 = A + lam_1[i] * m
    x_AB[:, i] = temp1.T
  return x_AB

def line_intersect(n1, A1, n2, A2):
  """Finds the intersection point of two lines defined by a normal and a point."""
  # The system of equations is N*x = p
  # where N = [n1.T; n2.T] and p = [n1.T@A1; n2.T@A2]
  N = np.block([[n1.T], [n2.T]])
  p = np.array([n1.T @ A1, n2.T @ A2])
  
  # Solve the system for the intersection point x
  P = np.linalg.solve(N, p)
  return P
