import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

handc1.gaussian.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double)
]

handc1.gaussian.restype = None

A = np.array([3,2], dtype = np.float64).reshape(-1,1)
B = np.array([4,-2], dtype = np.float64).reshape(-1,1)
C = np.array([10,2] , dtype = np.float64).reshape(-1,1)
X = np.zeros(2, dtype = np.float64).reshape(-1,1)

handc1.gaussian(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
    C.ctypes.data_as(ct.POINTER(ct.c_double)),
    X.ctypes.data_as(ct.POINTER(ct.c_double)),
)
print("Vector X = " , X)


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

P = np.array([6,-2], dtype = np.float64).reshape(-1,1)
Q = np.array([-6,7], dtype = np.float64).reshape(-1,1)
line(P,Q,"g-"," Line 1 ")
P = np.array([8,7], dtype = np.float64).reshape(-1,1)
Q = np.array([-8,-9], dtype = np.float64).reshape(-1,1)
line(P,Q,"r-"," Line 2 ")

plt.scatter(X[0,0], X[1,0])
plt.annotate(f"X\n({X[0,0]},{X[1,0]})",
                    (X[0], X[1]),
                    textcoords = "offset points" ,
                    xytext = (0,12),ha = "center")
plt.xlim([-1,4])
plt.ylim([-1,4])
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("5.2.35")

plt.savefig("../figs/intersect1.png")
plt.show()

#plt.savefig('../figs/intersect1.png')
#subprocess.run(shlex.split("termux-open ../figs/intersect1.png"))
