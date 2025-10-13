import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./generator.so")

handc1.circle_gen.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_int,
    ct.c_double
]

handc1.circle_gen.restype = None

O = np.zeros(2 , dtype = np.float64).reshape(-1,1)
X_cic = np.zeros(200, dtype = np.float64).reshape(-1,1)
Y_cic = np.zeros(200, dtype = np.float64).reshape(-1,1)

handc1.circle_gen(
    X_cic.ctypes.data_as(ct.POINTER(ct.c_double)),
    Y_cic.ctypes.data_as(ct.POINTER(ct.c_double)),
    O.ctypes.data_as(ct.POINTER(ct.c_double)),
    200 , 3 
)

handc1.points_gen.argtypes = [
    ct.POINTER(ct.c_double),
    ct.c_double,
    ct.c_double,
    ct.c_int
]

handc1.points_gen.restype = None


pt = 400
X_hyper_p = np.zeros(pt,dtype=np.float64).reshape(-1,1)
Y_hyper_p = np.zeros(pt,dtype=np.float64).reshape(-1,1)

handc1.points_gen(
    X_hyper_p.ctypes.data_as(ct.POINTER(ct.c_double)),
    0.1,
    30,
    pt 
)


X_hyper_n = np.zeros(pt,dtype=np.float64).reshape(-1,1)
Y_hyper_n = np.zeros(pt,dtype=np.float64).reshape(-1,1)

handc1.points_gen(
    X_hyper_n.ctypes.data_as(ct.POINTER(ct.c_double)),
    -30,
    -0.1,
    pt
)


handc1.hyper_gen.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_double,
    ct.c_int 
]

handc1.hyper_gen.restype = None

handc1.hyper_gen(
    X_hyper_p.ctypes.data_as(ct.POINTER(ct.c_double)),
    Y_hyper_p.ctypes.data_as(ct.POINTER(ct.c_double)),
    1,pt
)

handc1.hyper_gen(
    X_hyper_n.ctypes.data_as(ct.POINTER(ct.c_double)),
    Y_hyper_n.ctypes.data_as(ct.POINTER(ct.c_double)),
    1,pt
)

plt.figure()
plt.plot(X_cic,Y_cic,"blue",label= "Circle")
plt.plot(X_hyper_p,Y_hyper_p,"red",label="Rectangular Hyperbola")
plt.plot(X_hyper_n,Y_hyper_n,"red")

handc2 = ct.CDLL("./func.so")

handc2.calc.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.c_double,
    ct.c_double
]

handc2.calc.restype = ct.c_double

x = np.zeros(4,dtype=np.float64)
y = np.zeros(4,dtype=np.float64)

prod = handc2.calc(
    x.ctypes.data_as(ct.POINTER(ct.c_double)),
    y.ctypes.data_as(ct.POINTER(ct.c_double)),
    1 , 3
)
print("m_1m_2m_3m_4 = ",prod)
plt.scatter(x,y)
vert_labels = [r'$m_1$',r'$m_2$',r'$m_3$',r'$m_4$']

for i, txt in enumerate(vert_labels):
    plt.annotate(f'({txt},1/{txt})',
                 (x[i], y[i]),
                 textcoords="offset points",
                 xytext=(10,-15),
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.xlim([-10/2,10/2])
plt.ylim([-10/2,10/2])
plt.title("7.4.39")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.savefig("../figs/graph1.png")
plt.show()


