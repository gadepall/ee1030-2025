import ctypes

# Load shared library
lib = ctypes.CDLL('./main.so')
# Set argument and return types
lib.solve.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
lib.solve.restype = ctypes.c_char_p

# Call solve for 5x6 matrix of rank 4
def main():
    result = lib.solve(5, 6, 4).decode('utf-8')
    print(result)

if __name__ == '__main__':
    main()

