import ctypes

lib = ctypes.CDLL("./problem.so")

finalvector1=[0, 0]
finalvector2=[0, 0]

lib.get_vector1.argtypes = [ctypes.c_int]
lib.get_vector1.restype = ctypes.c_int

lib.get_vector2.argtypes = [ctypes.c_int]
lib.get_vector2.restype = ctypes.c_int

lib.get_constant1.argtypes = [ctypes.c_int]
lib.get_constant1.restype = ctypes.c_int

lib.get_constant2.argtypes = [ctypes.c_int]
lib.get_constant2.restype = ctypes.c_int


for i in range(0,2):
    finalvector1[i]=lib.get_vector1(i)-lib.get_vector2(i)

for i in range(0,2):
    finalvector2[i]=lib.get_vector1(i)+lib.get_vector2(i)

finalconstant=lib.get_constant1(0)+lib.get_constant2(0)

print(f"The final line equations are y=0 and {finalvector2[0]}x={finalconstant}")


