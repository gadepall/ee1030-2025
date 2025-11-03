import ctypes

# Load shared library
lib = ctypes.CDLL("./linear_system.so")

# Set return types
lib.classify_P.restype = ctypes.c_int
lib.classify_Q.restype = ctypes.c_int
lib.classify_R.restype = ctypes.c_int
lib.classify_S.restype = ctypes.c_int

systems = ["P", "Q", "R", "S"]
results = [
    lib.classify_P(),
    lib.classify_Q(),
    lib.classify_R(),
    lib.classify_S()
]

labels = {
    1: "Instability",
    2: "Inconsistency",
    3: "Non-uniqueness",
    4: "Exact"
}

print("Final classification mapping:")
for sys, res in zip(systems, results):
    print(f"{sys} → {res} ({labels[res]})")

