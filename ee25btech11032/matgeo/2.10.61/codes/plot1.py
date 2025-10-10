import ctypes
import numpy as np
import matplotlib.pyplot as plt
handc1 = ctypes.CDLL("./func.so")

handc1.norm_vec_sq.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]

handc1.norm_vec_sq.restype = ctypes.c_double

C = np.array([[2],[3],[4]], dtype= np.float64).reshape(-1,1)
print(C)
ab_sq = 29
m = 3
c_sq = handc1.norm_vec_sq(
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    m)

print(c_sq)
l = ab_sq / c_sq
ab1 = np.sqrt(l) * C
ab2 = -np.sqrt(l) * C

def line_cre(P: np.ndarray , Q: np.ndarray, str):
    handc2 = ctypes.CDLL("./line_gen.so")

    handc2.linegen.argtypes = [
        ctypes.POINTER(ctypes.c_double),
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
    Z_l = np.zeros(n,dtype=np.float64)
    handc2.linegen (
        X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Z_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        n,3
    )
    ax.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],[Z_l[0],Z_l[-1]],str)
O = np.array([[0],[0],[0]]).reshape(-1,1)
fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

line_cre(ab1,O,"g-")
line_cre(ab2,O,"r-")

coords = np.block([[ab1,ab2,O]])
ax.scatter(coords[0,:],coords[1,:],coords[2,:])
vert_labels = [r'$(a+b)_1$',r'$(a+b)_2$','O']

for i, txt in enumerate(vert_labels):
    if (coords[0,i] == 0 ) :
        ax.text(coords[0,i], coords[1,i] , coords[2,i],txt , ha='center', va = 'bottom')
    else :
        ax.text(coords[0,i], coords[1,i] , coords[2,i],f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f}, {coords[2,i]:.1f})',ha='center', va = 'bottom')
ax.scatter(coords[0,2], coords[1,2], coords[2,2], color="b", label="O : ORIGIN")
ax.legend(loc = "best")
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.grid()
plt.title("Fig:2.10.61")
ax.set_box_aspect([1,1,1])

fig.savefig("../figs/vector1.png")
fig.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))


