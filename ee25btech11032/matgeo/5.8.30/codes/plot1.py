import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

handc1.augment.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double)
]

handc1.augment.restype = None
A = np.array([60,100] , dtype = np.float64).reshape(-1,1)
B = np.array([240,200] , dtype = np.float64).reshape(-1,1)
C = np.array([4,25/6], dtype = np.float64).reshape(-1,1)

handc1.augment(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
    C.ctypes.data_as(ct.POINTER(ct.c_double))
)

print("Speed of Train : ",C[0]);
print("Speed of Bus : ",C[1]);

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
M = np.array([61/15,-1],dtype=np.float64).reshape(-1,1)
N = np.array([-10,151/60],dtype=np.float64).reshape(-1,1)
line(M,N,"g-","Line 1 ")
M = np.array([2+1/24 , -1],dtype=np.float64).reshape(-1,1)
N = np.array([-10,5+1/48],dtype=np.float64).reshape(-1,1)
line(M,N,"r-","Line 2")
plt.scatter(1/np.squeeze(C[0]),1/np.squeeze(C[1]))
plt.annotate(f"P\n(1/{np.squeeze(C[0]):.0f},1/{np.squeeze(C[1]):.0f})",(1/np.squeeze(C[0]),1/np.squeeze(C[1])),textcoords = "offset points" ,xytext = (0,-25),ha = "center")

plt.xlim([-1/2,1/2])
plt.ylim([-1/2,1/2])

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("5.8.30")

plt.savefig("../figs/Inter1.png")
plt.show()

#plt.savefig('../figs/Inter1.png')
#subprocess.run(shlex.split("termux-open ../figs/Inter1.png"))
