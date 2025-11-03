import ctypes
import os
import numpy as np  
import matplotlib.pyplot as plt 

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Load shared object
lib = ctypes.CDLL("./points.so")

lib.slope.argtypes = [ctypes.POINTER(ctypes.c_double*2),ctypes.POINTER(ctypes.c_double*2)]
lib.slope.restype = ctypes.c_double 

#Input 
a = (ctypes.c_double*2)(4,4)

b = (ctypes.c_double*2)(0,1)

sol = ctypes.c_double 
sol = lib.slope(a,b) 

print(f"The slope of the line is {sol}") 

#generating line 
x = np.linspace(-10,10,100)
y = b[1] + sol*(x - b[0]) 

#Plotting the line 
fig , ax = plt.subplots(figsize=(8,8)) 

ax.plot(x,y,'r',label="Line") 

ax.scatter(a[0],a[1],color="blue",label="A")
ax.text(a[0]+0.2,a[1],"A(4,p)",fontsize=10,color="blue")

ax.scatter(b[0],b[1],color="blue",label="B")
ax.text(b[0]+0.2,b[1],"B(0,q)",fontsize=10,color="blue")

# center axes
ax.axhline(0, color='black', linewidth=1) #draws x axes line at y=0 
ax.axvline(0, color='black', linewidth=1) #draws y axes line at x=0

# formatting
ax.set_aspect('equal') #make one unit on x the same as one unit on y , make equal units(scale for x and y)
ax.set_title("Line with slope = 0.75")
ax.legend()
ax.grid(True)

# save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "line.png"))
plt.show()

