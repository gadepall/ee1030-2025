import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

handc1.gp.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_double
]

handc1.gp.restype = None
O = np.zeros(2 , dtype = np.float64).reshape(-1,1)
A = np.array([1,2] , dtype = np.float64).reshape(-1,1)
B = np.zeros(2 , dtype = np.float64).reshape(-1,1)
C = np.zeros(2, dtype = np.float64).reshape(-1,1)
r = 3 

handc1.gp(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
    r
)

handc1.gp(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    C.ctypes.data_as(ct.POINTER(ct.c_double)),
    r**2
)

print("Vector A = " , A)
print("Vector B = " , B)
print("Vector C = " , C)


def line(P: np.ndarray , Q: np.ndarray, str1 , str2):
    handc2 = ct.CDLL("./line_gen.so")

    handc2.linegen.argtypes = [
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.c_int , ct.c_int
    ]

    handc2.linegen.restype = None
    n = 200
    XY = np.zeros((2,n),dtype=np.float64)

    handc2.linegen (
        XY.ctypes.data_as(ct.POINTER(ct.c_double)),
        P.ctypes.data_as(ct.POINTER(ct.c_double)),
        Q.ctypes.data_as(ct.POINTER(ct.c_double)),
        n,2
    )
    plt.plot(XY[0,:],XY[1,:], str1 , label = str2 )

plt.figure()

line(O,A,"g-"," Line Segment : OA ")
line(A,B,"r-"," Line Segment : AB ")
line(B,C,"b-"," Line Segment : BC ")

coords = np.block([[A,B,C,O]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['A','B','C','O']

for i , txt in enumerate(vert_label) :
    
    if i != 2 :
        plt.annotate(f"{txt}\n({coords[0,i]:.1f},{coords[1,i]:.1f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,12),ha = "center")
    else :
        plt.annotate(f"{txt}\n({coords[0,i]:.1f},{coords[1,i]:.1f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("4.13.37")

plt.savefig("../figs/colli1.png")
plt.show()

#plt.savefig('../figs/colli1.png')
#subprocess.run(shlex.split("termux-open ../figs/colli1.png"))
