import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc3 = ct.CDLL("./func.so")

handc3.solve.argtypes = [
    ct.c_double , ct.c_double , ct.c_double
]

handc3.solve.restype = ct.c_double
    
ans = handc3.solve (
    1,48,-324
)

print("Speed of Steam : ",ans)


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
    plt.plot(XY[0,:],XY[1,:], str1 , label = "Line" )

plt.figure()
P = np.array([-5,12],dtype=np.float64).reshape(-1,1)
S = np.array([10,-18],dtype=np.float64).reshape(-1,1)

line(S,P,"b")

T1 = np.array([1,0],dtype=np.float64).reshape(-1,1)
T2 = np.array([0,2],dtype=np.float64).reshape(-1,1)

coords = np.block([[T1,T2]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = [r't_1',r't_2']

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel('$Time: Downstream$')
plt.ylabel('$Time: Upstream$')

plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.xlim([-2,4])
plt.ylim([-2,4])
plt.title("9.4.45 - 1 ")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph1_1.png")
#plt.show()

def para(a,b,c, str1 , str2 ) : 
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
        -100,
        100,
        pt 
    )

    handc1.parabola.argtypes = [
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.c_double,ct.c_double,ct.c_double,
        ct.c_int 
    ]

    handc1.parabola.restype = None
    Y_p = np.zeros(pt,dtype=np.float64).reshape(-1,1)
    handc1.parabola(
        X_p.ctypes.data_as(ct.POINTER(ct.c_double)),
        Y_p.ctypes.data_as(ct.POINTER(ct.c_double)),
        a,b,c,pt
    )
      
    plt.plot(X_p,Y_p,str1,label=str2)
    
plt.figure()

para(1,48,-324,"b","Parabola")

T1 = np.array([6,0],dtype=np.float64).reshape(-1,1)
T2 = np.array([-54,0],dtype=np.float64).reshape(-1,1)

coords = np.block([[T1,T2]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = [r'k_1',r'k_2']

for i , txt in enumerate(vert_label) :
    plt.annotate(f"{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})",
                    (coords[0,i], coords[1,i]),
                    textcoords = "offset points" ,
                    xytext = (0,-25),ha = "center")

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
plt.grid(True) 
plt.axis('equal')
plt.xlim([-60,20])
plt.ylim([-20, 20 ])
plt.title("9.4.45 - 2 ")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph1.2.png")



