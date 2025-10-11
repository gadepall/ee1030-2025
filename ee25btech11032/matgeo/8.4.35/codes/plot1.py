import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

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
    plt.plot(XY[0,:],XY[1,:], str1  )

def ellipse(a,b, str1 , str2 ) : 
    handc1 = ct.CDLL("./generator.so")
    handc1.points_gen.argtypes = [
    ct.POINTER(ct.c_double),
    ct.c_double,
    ct.c_double,
    ct.c_int
    ]
    
    handc1.points_gen.restype = None

    pt = 40000

    X_el_p = np.zeros(pt,dtype=np.float64).reshape(-1,1)
    X_el_n = np.zeros(pt,dtype=np.float64).reshape(-1,1)
    Y_el_pp = np.zeros(pt,dtype=np.float64).reshape(-1,1)
    Y_el_np = np.zeros(pt,dtype=np.float64).reshape(-1,1)

    handc1.points_gen(
        X_el_p.ctypes.data_as(ct.POINTER(ct.c_double)),
        0.01,
        a,
        pt 
    )

    handc1.points_gen(
        X_el_n.ctypes.data_as(ct.POINTER(ct.c_double)),
        -a,
        -0.01,
        pt
    )

    handc1.ellipse_gen.argtypes = [
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.c_double,ct.c_double,
        ct.c_int 
    ]

    handc1.ellipse_gen.restype = None

    handc1.ellipse_gen(
        X_el_p.ctypes.data_as(ct.POINTER(ct.c_double)),
        Y_el_pp.ctypes.data_as(ct.POINTER(ct.c_double)),
        a,b,pt
    )

    handc1.ellipse_gen(
        X_el_n.ctypes.data_as(ct.POINTER(ct.c_double)),
        Y_el_np.ctypes.data_as(ct.POINTER(ct.c_double)),
        a,b,pt
    )

    Y_el_pn = - Y_el_pp 
    Y_el_nn = - Y_el_np
    
    plt.plot(X_el_p,Y_el_pp,str1,label=str2)
    plt.plot(X_el_p,Y_el_pn,str1)
    plt.plot(X_el_n,Y_el_np,str1)
    plt.plot(X_el_n,Y_el_nn,str1)
    
handc3 = ct.CDLL("./func.so")

handc3.e_val.argtypes = [
    ct.c_double , ct.c_double
]

handc3.e_val.restype = ct.c_double
    
e = handc3.e_val (
    (12**(1/2)),(16**(1/2))
)

print("e : ",e)


plt.figure()

P = np.array([3,2],dtype=np.float64).reshape(-1,1)
T = np.array([-3,2],dtype=np.float64).reshape(-1,1)
R = np.array([3,-2],dtype=np.float64).reshape(-1,1)
S = np.array([-3,-2],dtype=np.float64).reshape(-1,1)

line(P,T,"b")
line(T,S,"b")
line(P,R,"b")
line(S,R,"b")

ellipse(3,2,"r","Ellipse 1")
ellipse((12**(1/2)),(16**(1/2)),"g","Ellipse 2")

Q = np.array([0,4],dtype=np.float64).reshape(-1,1)

coords = np.block([[P,T,R,S,Q]])

plt.scatter(coords[0,:] , coords[1,:])
vert_label = ['P','M','R','S','Q']

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
#plt.xlim([-10/2,10/2])
#plt.ylim([-10/2,10/2])
plt.title("8.4.35")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph1.png")
plt.show()


