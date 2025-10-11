import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

handc1.solve.argtypes = [
    ct.c_double , ct.c_double , ct.c_double
]

handc1.solve.restype = ct.c_double
    
ans = handc1.solve (
    1,-2,1
)
if ans == 1 :
    print("Line is tangent!")
else :
    print("Line is not tangent!");


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

P = np.array([-10,-9],dtype=np.float64).reshape(-1,1)
S = np.array([20,21],dtype=np.float64).reshape(-1,1)

line(S,P,"g")

def para(a, str1 , str2 ) : 
    handc1 = ct.CDLL("./generator.so")
    handc1.points_gen.argtypes = [
    ct.POINTER(ct.c_double),
    ct.c_double,
    ct.c_double,
    ct.c_int
    ]
    
    handc1.points_gen.restype = None

    pt = 40000

    X_p = np.zeros(pt,dtype=np.float64).reshape(-1,1)
    
    handc1.points_gen(
        X_p.ctypes.data_as(ct.POINTER(ct.c_double)),
        0,
        100,
        pt 
    )

    handc1.parabola.argtypes = [
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.c_double,
        ct.c_int 
    ]

    handc1.parabola.restype = None
    Y_p = np.zeros(pt,dtype=np.float64).reshape(-1,1)
    handc1.parabola(
        X_p.ctypes.data_as(ct.POINTER(ct.c_double)),
        Y_p.ctypes.data_as(ct.POINTER(ct.c_double)),
        a,pt
    )
    
    Y_n = -Y_p
      
    plt.plot(X_p,Y_p,str1,label=str2)
    plt.plot(X_p,Y_n,str1)
    
para(1,"r","Parabola")

T1 = np.array([1,2],dtype=np.float64).reshape(-1,1)

coords = np.block([[T1]])

plt.scatter(coords[0,:] , coords[1,:], label = "Point of Tangancy")
vert_label = ['Q']

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
plt.xlim([-2,10])
plt.ylim([-8,8])
plt.title("10.4.8")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph1.png")
plt.show()


