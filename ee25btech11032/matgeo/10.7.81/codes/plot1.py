import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./generator.so")
def cir(P: np.ndarray , r , str1 ,str2) : 
    handc1.circle_gen.argtypes = [
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.c_int,
        ct.c_double
    ]

    handc1.circle_gen.restype = None

    
    X_cic = np.zeros(200, dtype = np.float64).reshape(-1,1)
    Y_cic = np.zeros(200, dtype = np.float64).reshape(-1,1)

    handc1.circle_gen(
        X_cic.ctypes.data_as(ct.POINTER(ct.c_double)),
        Y_cic.ctypes.data_as(ct.POINTER(ct.c_double)),
        P.ctypes.data_as(ct.POINTER(ct.c_double)),
        200 , r 
    )
    plt.plot(X_cic,Y_cic,str1,label=str2)
    
def line(P: np.ndarray , Q: np.ndarray, str1  ):
    handc2 = ct.CDLL("./generator.so")

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
    plt.plot(XY[0,:],XY[1,:], str1 , label = "Tangent" )


plt.figure()

P = np.array([15,-50/3],dtype=np.float64).reshape(-1,1)
Q = np.array([-15,70/3],dtype=np.float64).reshape(-1,1)
T = np.array([1,2],dtype=np.float64).reshape(-1,1)
U = np.array([4/5,3/5],dtype=np.float64).reshape(-1,1)
line(P,Q,"g")
'''
O1 = np.array([5,5],dtype=np.float64).reshape(-1,1)
O2 = np.array([-3,-1],dtype=np.float64).reshape(-1,1)
cir(O1,5,"r","Circle 1")
cir(O2,5,"b","Circle 2")
'''
handc2 = ct.CDLL("./func.so")

handc2.calc.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_double,
]

handc2.calc.restype = None

O1 = np.zeros(2,dtype=np.float64).reshape(-1,1)
O2 = np.zeros(2,dtype=np.float64).reshape(-1,1)

prod = handc2.calc(
    T.ctypes.data_as(ct.POINTER(ct.c_double)),
    U.ctypes.data_as(ct.POINTER(ct.c_double)),
    O1.ctypes.data_as(ct.POINTER(ct.c_double)),
    O2.ctypes.data_as(ct.POINTER(ct.c_double)),
    5
)

cir(O1,5,"r","Circle 1")
cir(O2,5,"b","Circle 2")

coords = np.block([[T,O1,O2]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['P',r'$O_1$',r'$O_2$']

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.xlim([-10,10])
plt.ylim([-10,12])
plt.title("10.7.81")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph1.png")
plt.show()


