import ctypes
import numpy as np
import os

# Load shared library
lib = ctypes.CDLL(os.path.abspath('./code.so'))

a1 = ctypes.c_double()
a2 = ctypes.c_double()
c1 = ctypes.c_double()
c2 = ctypes.c_double()

# call C function
lib.get_line_params(ctypes.byref(a1), ctypes.byref(a2), ctypes.byref(c1), ctypes.byref(c2))

# Extract values
roots = [a1.value, a2.value]
cs = [c1.value, c2.value]

# Save to numpy for plot
np.save('roots.npy', np.array(roots))
np.save('cs.npy', np.array(cs))

print("Roots (a1, a2):", roots)
print("Constants (c1, c2):", cs)

