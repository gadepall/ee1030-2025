import ctypes
import numpy as np
import matplotlib.pyplot as plt

handc1 = ctypes.CDLL("./formula.so")

handc1.func.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
]
handc1.func.restype = None # void function

m = 2

P = np.array([[-2],[2]], dtype=np.float64)
B = np.array([[3],[4]], dtype=np.float64)
A = np.zeros(m, dtype=np.float64)

handc1.func(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    m #len(P) alternate
)


handc1.radius.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]

handc1.radius.restype = ctypes.c_double #return double

radius = handc1.radius(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    m
)

handc2 = ctypes.CDLL("./circle_line.so")
handc2.line_gen.argtypes = [

    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.c_int
]

handc2.line_gen.restype = None

n = 20
m = 2

X_l = np.zeros(n,dtype=np.float64)
Y_l = np.zeros(n,dtype=np.float64)

handc2.line_gen(

    X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    n,m
)
plt.figure()

#plotting line

plt.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],"g--",label="Diameter")


plt.scatter(A[0],A[1],color = "red",s=50)
plt.scatter(B[0],B[1],color = "red",s=50)
plt.scatter(P[0],P[1],color = "red",s=50,label = "Center of Circle")

handc2.circle_gen.argtypes = [

    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.c_double
]

handc2.circle_gen.restypes = None

n = 200
#r = radius 

X_c =  np.zeros(n,dtype=np.float64)
Y_c =  np.zeros(n,dtype=np.float64)

handc2.circle_gen(

    X_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    Y_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    n , radius
)

#plotting circle
plt.plot(X_c,Y_c , "b-")

plt.annotate(f"A({A[0]},{A[1]})", (A[0], A[1]), textcoords="offset points", xytext=(0,5), ha='right')
plt.annotate("B", (B[0], B[1]), textcoords="offset points", xytext=(0,5), ha='left')
plt.annotate("P", (P[0], P[1]), textcoords="offset points", xytext=(0,5), ha='left')

# Equal scaling for axes (important for circles!)
plt.gca().set_aspect("equal", adjustable="box")

plt.xlim([-10,6])
plt.ylim([-4,10])

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("1.5.20")

plt.legend(loc = 'upper right')
plt.grid(True)

# Save and showueraio
plt.savefig("../figs/circle_graph.png")
plt.show()
