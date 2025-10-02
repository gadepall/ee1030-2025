import ctypes

lib = ctypes.CDLL("./libinverse.so")
lib.inverse.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]
lib.inverse.restype = ctypes.c_int

# Input each element individually
a11 = float(input("Enter mat[1][1]: "))
a12 = float(input("Enter mat[1][2]: "))
a21 = float(input("Enter mat[2][1]: "))
a22 = float(input("Enter mat[2][2]: "))

# Create ctypes array row-wise
mat_array = (ctypes.c_double * 4)(a11, a12, a21, a22)
res_array = (ctypes.c_double * 4)()

# Call C function
status = lib.inverse(mat_array, res_array)

if status == 0:
    print("Matrix is singular, inverse does not exist.")
else:
    inv_matrix = [[res_array[0], res_array[1]],
                  [res_array[2], res_array[3]]]
    print("Inverse matrix:")
    for row in inv_matrix:
        print(row)
