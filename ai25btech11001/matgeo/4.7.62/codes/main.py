from ctypes import *

filename = './libmain.so'


# Load the shared object file (pgm.so)
clib = CDLL(filename)

class Vec3(Structure):
    _fields_ = [('x',c_float)
                ,('y',c_float)
                ,('z',c_float)]
    def __init__(self,x, y,z):
        super().__init__()
        self.x=x
        self.y=y
        self.z=z

dotVec3 = clib.dotVec3
dotVec3.restype=c_int
dotVec3.argtypes=[Vec3,Vec3]

A,B = Vec3(2,3,-1),Vec3(5,2,-4)
print(f"Dot prodouct of n and P ={dotVec3(A,B)}")



