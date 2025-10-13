import ctypes
import os

so_file = "./matrix.so"

lib = ctypes.CDLL(so_file)

# The C code has main() printing everything,
# so we can just call it directly.
# But we could also expose a solve function if needed.

print("Running matrix problem solver (C code)...\n")

# Call C's main() function
lib.main()

print("\nExecution complete (Python successfully called C code).")

