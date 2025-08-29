import ctypes
import numpy as np

lib = ctypes.CDLL("./problem.so")


points = (ctypes.c_double * 6)()
lib.get_points(points)


pts = np.array(points).reshape(3,2)
R, Q, P = pts


M = (Q + P) / 2


median_vec = M - R
median_length = np.linalg.norm(median_vec)


print("R =", R)
print("Q =", Q)
print("P =", P)
print("Midpoint of QP =", M)
print("Median RM length =", median_length)

