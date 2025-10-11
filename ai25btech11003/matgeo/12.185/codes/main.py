import ctypes

# Load the shared library
lib = ctypes.CDLL("./main.so")
lib.get_rank.restype = ctypes.c_int

# Call C function to compute rank
rank_from_c = lib.get_rank()

# Read the rank from main.dat
with open("main.dat") as f:
    rank_from_dat = int(f.read().strip())

# Verify consistency
if rank_from_c != rank_from_dat:
    raise ValueError("Mismatch between C output and data file!")

# Determine correct statement
if rank_from_c == 4:
    answer = "Option A: Q has four linearly independent rows and four linearly independent columns."
else:
    answer = "No valid option for rank = {}".format(rank_from_c)

print(answer)

