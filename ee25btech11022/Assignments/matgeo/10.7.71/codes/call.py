# call.py
import ctypes
import numpy as np

def get_points():
    lib = ctypes.CDLL('./code.so')
    arr = (ctypes.c_double * 10)()
    lib.get_points(arr)
    return np.array(list(arr))

if __name__ == "__main__":
    pts = get_points()
    print(pts.reshape(-1, 2))

