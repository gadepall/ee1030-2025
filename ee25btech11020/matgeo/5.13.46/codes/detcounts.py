import ctypes

lib = ctypes.CDLL("./libdetcounts.so")  

lib.compute_counts.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.compute_counts.restype = None

counts = (ctypes.c_int * 7)()

lib.compute_counts(counts)

for d in range(-3, 4):
    if counts[d+3] > 0:
        print(f"det = {d}: {counts[d+3]} matrices")

