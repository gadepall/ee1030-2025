import ctypes
import numpy as np
import matplotlib.pyplot as plt
def length_func (P: np.ndarray , Q: np.ndarray, m ) -> float:
    handc1 = ctypes.CDLL("./length.so")

    handc1.length.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int
    ]

    handc1.length.restype = ctypes.c_double

    len = handc1.length (
        P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        m
    )
    return len

A = np.array([[-2],[1]], dtype=np.float64)
B = np.array([[1],[0]], dtype=np.float64)
C = np.array([[4],[1]], dtype=np.float64)
D = np.array([[1],[2]], dtype=np.float64)

d1 = length_func(A,B,2)
d2 = length_func(B,C,2)

if d1 == d2 :
    print("Length of Sides =",d1)
else:
    print("Length of Side AB and CD = ",d1)
    print("Length of Side BC and AD = ",d2)

def line_cre(P: np.ndarray , Q: np.ndarray, str):
    handc2 = ctypes.CDLL("./line_gen.so")

    handc2.linegen.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int , ctypes.c_int
    ]

    handc2.linegen.restype = None
    n = 200
    X_l = np.zeros(n,dtype=np.float64)
    Y_l = np.zeros(n,dtype=np.float64)

    handc2.linegen (
        X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        n,2
    )
    plt.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],str)



plt.figure()

line_cre(A,B,"g-")
line_cre(B,C,"r-")
line_cre(C,D,"b-")
line_cre(D,A,"y-")

coords = np.block([[A,B,C,D]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = ['A','B','C','D']
#for i , txt in enumerate(vert_labels):
 #   plt.annotate(txt,(coords[0,i],coords[1,i]),textcoords="offset points", xytext=(0,10),ha='center')

for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.0f}, {coords[1,i]:.0f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(20,0),
                 ha='center')


plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid()

plt.title("Fig:1.9.21")
plt.axis('equal')

plt.savefig("../figs/p_gram1.png")
plt.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))


