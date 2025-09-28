from ctypes import CDLL, c_double, POINTER

# Load the shared library
lib = CDLL('./libtriangle.so')

# Setup argument types
lib.find_third_vertex.argtypes = [POINTER(c_double), POINTER(c_double)]

def find_third_vertex():
    x = c_double()
    y = c_double()
    lib.find_third_vertex(x, y)
    return x.value, y.value

if __name__ == "__main__":
    cx, cy = find_third_vertex()
    print(f"Third vertex coordinates from C code: ({cx}, {cy})")

