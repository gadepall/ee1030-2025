import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

handc1.norm_sq.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_int
]

handc1.norm_sq.restype = ct.c_double

A = np.array([[-4],[-6]] , dtype = np.float64).reshape(-1,1)
B = np.array([[-1],[7]] , dtype = np.float64).reshape(-1,1)
P = np.array([[-34/13] ,[ 0 ]] , dtype = np.float64).reshape(-1,1)

norm = handc1.norm_sq(
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
    P.ctypes.data_as(ct.POINTER(ct.c_double)),
    2
)

handc1.ratio.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_double
]
handc1.ratio.restype = ct.c_double

k = handc1.ratio(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
    P.ctypes.data_as(ct.POINTER(ct.c_double)),norm
)

print("The ratio : " , k )

def line(P : np.ndarray , Q : np.ndarray , str ) :

    handc2 = ct.CDLL("./line_gen.so")
    handc2.line_cre.argtypes = [
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.c_int,ct.c_int
    ]
    n = 200
    X_l = np.zeros(n,dtype=np.float64)
    Y_l = np.zeros(n,dtype=np.float64)

    handc2.line_cre.restype = None

    handc2.line_cre(
        X_l.ctypes.data_as(ct.POINTER(ct.c_double)),
        Y_l.ctypes.data_as(ct.POINTER(ct.c_double)),
        P.ctypes.data_as(ct.POINTER(ct.c_double)),
        Q.ctypes.data_as(ct.POINTER(ct.c_double)),
        n,2
    )

    plt.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]], str , label = "Line Segment AB")

plt.figure()

line(A,B,"g--")

coords = np.block([[A,B,P]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['A', 'B' , 'P' ]

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.1f},{coords[1,i]:.1f})",
                 (coords[0,i], coords[1,i]),
                 textcoords = "offset points" ,
                 xytext = (10,20),ha = "center")

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()

plt.legend(loc="best")

plt.title("4.3.21")

plt.savefig("../figs/section1.png")
plt.show()
