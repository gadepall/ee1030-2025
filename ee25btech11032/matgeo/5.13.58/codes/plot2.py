import math
import sys
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from line.funcs import *

i = 1 
O = np.zeros(3,dtype=np.float64).reshape(-1,1)

def plot_it(P,Q,str):
    global i 
    x_l = line_gen_num(P,Q,20)
    if i == 1 : 
        ax.plot(x_l[0,:],x_l[1,:],x_l[2,:] , str , label = "Correct Solution"  )
    elif i == 2 :
        ax.plot(x_l[0,:],x_l[1,:],x_l[2,:] , str , label = "Inorrect Solution")
    else :
        ax.plot(x_l[0,:],x_l[1,:],x_l[2,:] , str)
    i += 1 

fig = plt.figure()

ax = fig.add_subplot(111,projection="3d")
# let omega correspond to 1 and omega square to -1 

p1 = np.array([1,1,1],dtype=np.float64).reshape(-1,1)
p2 = np.array([-1,1,1],dtype=np.float64).reshape(-1,1)
p3 = np.array([1,-1,1],dtype=np.float64).reshape(-1,1)
p4 = np.array([1,1,-1],dtype=np.float64).reshape(-1,1)
p5 = np.array([1,-1,-1],dtype=np.float64).reshape(-1,1)
p6 = np.array([-1,1,-1],dtype=np.float64).reshape(-1,1)
p7 = np.array([-1,-1,1],dtype=np.float64).reshape(-1,1)
p8 = np.array([-1,-1,-1],dtype=np.float64).reshape(-1,1)

plot_it(p1,O,"g-")
plot_it(p2,O,"r-")
plot_it(p3,O,"g-")
plot_it(p4,O,"r-")
plot_it(p5,O,"r-")
plot_it(p6,O,"r-")
plot_it(p7,O,"r-")
plot_it(p8,O,"r-")


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

fig.savefig("../figs/vector2.png")
fig.show()
#plt.savefig('../figs/vector2.png')
#subprocess.run(shlex.split("termux-open ../figs/vector2.png"))
