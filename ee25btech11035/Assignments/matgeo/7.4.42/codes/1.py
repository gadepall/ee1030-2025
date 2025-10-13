import ctypes
import os

# Construct the full path to the library in the current directory
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1.so')
c_library = ctypes.CDLL(lib_path)

c_function = c_library.hasTwoDistinctChords
c_function.argtypes = [ctypes.c_double]  # Argument is a C double
c_function.restype = ctypes.c_bool      # Return type is a C bool

if __name__ == "__main__":
    test_cases = [3.0, -5.0, 1.5, 2.0]
    
    for a_value in test_cases:
        result = c_function(a_value)
        print(f"For a = {a_value:.2f}, the condition is {result}")
