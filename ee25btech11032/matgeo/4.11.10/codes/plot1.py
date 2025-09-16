import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

handc1.section_formula.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_double,
    ct.c_int
]

handc1.section_formula.restype = None

X = np.array([6,-6] , dtype = np.float64).reshape(-1,1)
Y = np.array([-4,-1] , dtype = np.float64).reshape(-1,1)
A = np.zeros(2, dtype = np.float64).reshape(-1,1)
p = 2 / 3

handc1.section_formula(
    X.ctypes.data_as(ct.POINTER(ct.c_double)),
    Y.ctypes.data_as(ct.POINTER(ct.c_double)),
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    p , 2
)

print("Vector A = ",A)

M = np.array([-10,14] , dtype = np.float64).reshape(-1,1)
N = np.array([10,-16] , dtype = np.float64).reshape(-1,1)

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

line(X,Y,"g--","Line Segment XY")
line(M,N,"r-","Line Containing A")
coords = np.block([[X,Y,A]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['X', 'Y' , 'A' ]

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.1f},{coords[1,i]:.1f})",
                 (coords[0,i], coords[1,i]),
                 textcoords = "offset points" ,
                 xytext = (0,-30),ha = "center")

plt.xlim([-6,8])
plt.ylim([-8,0])
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("4.11.10")

plt.savefig("../figs/section1.png")
plt.show()

#plt.savefig('../figs/section1.png')
#subprocess.run(shlex.split("termux-open ../figs/section1.png"))
