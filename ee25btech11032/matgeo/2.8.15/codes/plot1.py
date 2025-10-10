import ctypes
import numpy as np
import matplotlib.pyplot as plt
handc1 = ctypes.CDLL("./func.so")

handc1.calc.argtypes=[
    ctypes.c_double,
    ctypes.c_double
]

theta1 = 60
theta2 = 45

l = np.cos(np.deg2rad(theta1))
m = np.cos(np.deg2rad(theta2))

handc1.calc.restype = ctypes.c_double

n = handc1.calc(
    l , m
)

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
print(n)
l = 10 * l
n *= 10
m *= 10
A1 = np.array([[l],[m],[n]],dtype=np.float64).reshape(-1,1)
A2 = np.array([[l],[m],[-n]], dtype= np.float64).reshape(-1,1)
B = np.array([[0],[0],[0]]).reshape(-1,1)
fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

line_cre(A1,B,"g-")
line_cre(A2,B,"r-")

coords = np.block([[A1,A2,B]])
ax.scatter(coords[0,:],coords[1,:],coords[2,:])
vert_labels = [r'$A_1$',r'$A_2$','O']

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
#ax.legend(loc='best')
ax.grid()
ax.set_xlim([-2, 7])
ax.set_ylim([-2,8])
ax.set_zlim([-6,6])
plt.title("Fig:2.8.15")
#ax.set_box_aspect([1,1,1])

fig.savefig("../figs/vector1.png")
fig.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))


