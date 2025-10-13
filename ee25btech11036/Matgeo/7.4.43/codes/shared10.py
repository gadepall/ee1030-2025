import ctypes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Load shared library
lib = ctypes.CDLL("./libgeom.so")

class Vec(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

# Bind functions
lib.circle_center.argtypes = [Vec, Vec]
lib.circle_center.restype = Vec

lib.midpoint_DC.argtypes = [Vec, Vec]
lib.midpoint_DC.restype = Vec

# Shift circle upward for clarity
A = Vec(0,1)
C = Vec(2,1)
B = Vec(1,2)
D = Vec(1.5,1.5)

O = lib.circle_center(A,C)
M = lib.midpoint_DC(D,C)

# Convert to numpy
def vec2np(v): return np.array([v.x, v.y])
An,Bn,Cn,Dn,On,Mn = map(vec2np,[A,B,C,D,O,M])

# Circle
r = np.linalg.norm(Cn - An)/2
theta = np.linspace(0,2*np.pi,400)
circle_x = On[0] + r*np.cos(theta)
circle_y = On[1] + r*np.sin(theta)

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(circle_x, circle_y, 'b')

# Points
for P,name in zip([An,Bn,Cn,Dn,Mn,On],['A','B','C','D','M','O']):
    ax.plot(P[0],P[1],'ro')
    ax.text(P[0]+0.05,P[1]+0.05,name,fontsize=12)

# Lines
ax.plot([Bn[0],Cn[0]],[Bn[1],Cn[1]],'g--',label="$BC$")
ax.plot([An[0],Dn[0]],[An[1],Dn[1]],'m--',label="$AD$")
ax.plot([An[0],Cn[0]],[An[1],Cn[1]],'k-', label="$AC$")
ax.plot([An[0],Bn[0]],[An[1],Bn[1]],'c-', label="$AB$")  # New AB

# Function to draw arcs for angles
def draw_angle(ax, center, p1, p2, radius=0.25, label=""):
    ang1 = np.degrees(np.arctan2(p1[1]-center[1], p1[0]-center[0]))
    ang2 = np.degrees(np.arctan2(p2[1]-center[1], p2[0]-center[0]))
    arc = Arc(center, 2*radius, 2*radius, angle=0,
              theta1=min(ang1,ang2), theta2=max(ang1,ang2),
              color='k')
    ax.add_patch(arc)
    mid = (ang1+ang2)/2
    ax.text(center[0]+radius*np.cos(np.radians(mid)),
            center[1]+radius*np.sin(np.radians(mid)),
            label, fontsize=14, color="red")

# Angles at A
draw_angle(ax, An, Dn, Bn, radius=0.3, label=r"$\alpha$")
draw_angle(ax, An, Cn, Bn, radius=0.5, label=r"$\beta$")

# Aesthetics
ax.set_aspect(1)
ax.set_xlim(-0.5,2.5)
ax.set_ylim(0,2.5)
ax.legend(fontsize=10, loc="upper right")
plt.show()

