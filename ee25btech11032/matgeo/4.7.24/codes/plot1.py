import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

handc1.dot_prod.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_int
]

handc1.dot_prod.restype = ct.c_double

A = np.array([2,3], dtype= np.float64).reshape(-1,1)
B = np.array([3,-1] , dtype= np.float64 ).reshape(-1,1)

P = np.array([5,2] , dtype= np.float64 ).reshape(-1,1)
K = (B-A) 
const = handc1.dot_prod(
    K.ctypes.data_as(ct.POINTER(ct.c_double)),
    P.ctypes.data_as(ct.POINTER(ct.c_double)),
    2
)
K = K.reshape(1,-1)
print("Required Line Equation : ")
print(K,"X = ", const )

def line_cre(P: np.ndarray , Q: np.ndarray, str1 , str2):
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
#the ratio of perp on Line Ab is 7:10 
line_cre(P,(10 * A+ 7 * B)/17,"g-","Required Line")
line_cre(A,B,"r--" , "Line AB")

coords = np.block([[A,B,P, (10 * A+ 7 * B)/17 ]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = ['A','B','P','Q']

for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(25,-12),
                 ha='center', va = 'bottom')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.title("Fig:4.7.24")
plt.axis('equal')

plt.savefig("../figs/perpendicular1.png")
plt.show()

#plt.savefig('../figs/perpendicular1.png')
#subprocess.run(shlex.split("termux-open ../figs/perpendicular1.png"))


