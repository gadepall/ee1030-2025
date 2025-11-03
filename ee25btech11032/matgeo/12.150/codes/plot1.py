import ctypes
import numpy as np
import matplotlib.pyplot as plt
handc1 = ctypes.CDLL("./func.so")

handc1.cross.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

handc1.cross.restype = ctypes.c_double
a = np.array([1, 1, 1],dtype=np.float64)
b = np.array([-1, -1, 1],dtype=np.float64)
a=a.reshape(-1,1)
b=b.reshape(-1,1)
origin= np.zeros(3,dtype=np.float64).reshape(-1,1)
C = np.zeros(3, dtype= np.float64).reshape(-1,1)

handc1.cross(
    a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
)

print("a x b = ",C)


def line_cre(P: np.ndarray , Q: np.ndarray, str1 , str2 ):
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
    ax.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],[Z_l[0],Z_l[-1]],str1, label = str2)

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

line_cre(origin,a,"r","side a")
line_cre(origin,b,"orange","side b")
line_cre(origin,C,"g","")
line_cre(a,b,"b","side a+b")

coords = np.block([[a,b,C,origin]])
plt.scatter(coords[0,:],coords[1,:],coords[2,:])
vert_labels = [r'$a$',r'$b$',r'$a\times b$',"O"]
for i, txt in enumerate(vert_labels):
   ax.text(coords[0,i], coords[1,i] , coords[2,i],f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f}, {coords[2,i]:.1f})',ha='center', va = 'bottom')

ax.scatter(coords[0,3], coords[1,3], coords[2,3], color="b", label="O : ORIGIN")


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc = "best")
ax.legend(loc='upper left', bbox_to_anchor=(.90, 1.10))
ax.grid()
plt.title("Fig:12.150")
ax.set_box_aspect([1,1,1])

fig.savefig("../figs/vector1.png")
fig.show()
#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))

