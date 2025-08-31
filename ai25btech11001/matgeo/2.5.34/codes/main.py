from ctypes import *

filename = './libmain.so'


# Load the shared object file (pgm.so)
clib = CDLL(filename)

class Vec2(Structure):
    _fields_ = [('x',c_float),('y',c_float)]
    def __init__(self,x, y):
        super().__init__()
        self.x=x
        self.y=y
    def __sub__(self,other):
        return Vec2(self.x-other.x,self.y-other.y)


dotVec2 = clib.dotVec2
dotVec2.restype=c_int
dotVec2.argtypes=[Vec2,Vec2]

A,B,C = Vec2(-2,3),Vec2(8,3),Vec2(6,7)
a=B-C
b=A-C
c=A-B
print(f"Dot prodouct of a and b ={dotVec2(a,b)}")
print(f"Dot prodouct of a and c ={dotVec2(a,c)}")
print(f"Dot prodouct of b and c ={dotVec2(b,c)}")



