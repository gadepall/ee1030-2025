# call.py
import ctypes
import numpy as np

lib = ctypes.CDLL('./points.so')  # Shared object must be in working dir

PointsArr = ctypes.c_double * 4
pts = PointsArr()

lib.tangent_points(pts)  # Fill pts with tangent points

points = np.array([pts[0], pts[1], pts[2], pts[3]]).reshape(2, 2)

