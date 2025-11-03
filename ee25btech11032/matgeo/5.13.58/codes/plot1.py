import ctypes
import numpy as np
import matplotlib.pyplot as plt

i = 1 
def line_cre(P: np.ndarray , Q: np.ndarray, str):
    handc1 = ctypes.CDLL("./line_gen.so")
    global i 
    handc1.linegen.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int , ctypes.c_int
    ]
    handc1.linegen.restype = None
    n = 200
    X_l = np.zeros(n,dtype=np.float64)
    Y_l = np.zeros(n,dtype=np.float64)
    Z_l = np.zeros(n,dtype=np.float64)
    handc1.linegen (
        X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Z_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        n,3
    )
     
    if i == 1 :
        ax.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],[Z_l[0],Z_l[-1]],str,label = "Correct Solution" )
    elif i == 2 : 
        ax.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],[Z_l[0],Z_l[-1]],str,label = "Incorrect Solution" )
    else :
        ax.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],[Z_l[0],Z_l[-1]],str)
    i=i+1

fig = plt.figure()

ax = fig.add_subplot(111,projection="3d")
# let omega correspond to 1 and omega square to -1 
O = np.zeros(3,dtype=np.float64).reshape(-1,1)
p1 = np.array([1,1,1],dtype=np.float64).reshape(-1,1)
p2 = np.array([-1,1,1],dtype=np.float64).reshape(-1,1)
p3 = np.array([1,-1,1],dtype=np.float64).reshape(-1,1)
p4 = np.array([1,1,-1],dtype=np.float64).reshape(-1,1)
p5 = np.array([1,-1,-1],dtype=np.float64).reshape(-1,1)
p6 = np.array([-1,1,-1],dtype=np.float64).reshape(-1,1)
p7 = np.array([-1,-1,1],dtype=np.float64).reshape(-1,1)
p8 = np.array([-1,-1,-1],dtype=np.float64).reshape(-1,1)

line_cre(p1,O,"g-")
line_cre(p2,O,"r-")
line_cre(p3,O,"g-")
line_cre(p4,O,"r-")
line_cre(p5,O,"r-")
line_cre(p6,O,"r-")
line_cre(p7,O,"r-")
line_cre(p8,O,"r-")


coords = np.block([[p1,p2,p3,p4,p5,p6,p7,p8]])
ax.scatter(coords[0,:],coords[1,:],coords[2,:])
vert_labels = [r'$p_1$',r'$p_2$',r'$p_3$',r'$p_4$',r'$p_5$',r'$p_6$',r'$p_7$',r'$p_8$']

for i, txt in enumerate(vert_labels):
    ax.text(coords[0,i], coords[1,i] , coords[2,i],f'{txt}\n({coords[0,i]:.0f}, {coords[1,i]:.0f}, {coords[2,i]:.0f})',ha='center', va = 'bottom')
        
ax.scatter(0, 0, 0, color="black", label="ORIGIN")
ax.text(0,0,0,"",ha='left')
#ax.legend(loc = "upper right")
ax.legend(loc='upper left', bbox_to_anchor=(.80, 1.05))
ax.set_xlabel('$a$')
ax.set_ylabel('$b$')
ax.set_zlabel('$c$')
#ax.legend(loc='best')
ax.grid()
plt.title("Fig:5.13.58")
#ax.set_box_aspect([1,1,1])

fig.savefig("../figs/vector1.png")
fig.show()
#plt.savefig('../figs/vector1.png')
#subprocess.run(shlex.split("termux-open ../figs/vector1.png"))
