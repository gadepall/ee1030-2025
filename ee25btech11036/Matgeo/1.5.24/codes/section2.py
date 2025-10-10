import sys                            # for path to external scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

# --- Step 1: Rank Matrix condition ---
print("Step 1: Rank condition between b and c")
print("Take M = (2,-5), P = (0,b), Q = (c,0)")

# Construct rank matrix for collinearity of P, Q, M
# Vectors (P-M) and (Q-M) must be linearly dependent => rank = 1
# Matrix form: [[Px-Mx, Qx-Mx], [Py-My, Qy-My]]
# Here M=(2,-5)
M = np.array(([2, -5])).reshape(-1,1)
b, c = symbols = (None, None)  # placeholders for explanation

print("Matrix formed from (P-M) and (Q-M):")
print("[[-2, c-2], [b+5, 5]]")

print("Row operation: R2 -> -2*R2 - (b+5)*R1")
print("=> [[-2, c-2], [0, -10 - (b+5)(c-2)]]")

print("For rank=1: (b+5)(c-2) = -10   (Relation 1)\n")

# --- Step 2: Midpoint relation ---
print("Step 2: Midpoint relation")
print("Midpoint M = ((0+c)/2, (b+0)/2) = (2, -5)")

c = 2 * M[0,0]
b = 2 * M[1,0]
print(f"c/2 = 2  =>  c = {c}")
print(f"b/2 = -5 =>  b = {b}   (Relation 2)\n")

# --- Step 3: Solve both relations ---
P = np.array(([0,b])).reshape(-1,1)
Q = np.array(([c,0])).reshape(-1,1)

print("Step 3: Solve")
print(f"Coordinates of P = (0, {b})")
print(f"Coordinates of Q = ({c}, 0)\n")

# --- Step 4: Verification ---
mid = (P+Q)/2
print("Verification: midpoint of P and Q =", mid.ravel())

# --- Step 5: Plotting ---
x_PQ = line_gen(P,Q)
plt.plot(x_PQ[0,:], x_PQ[1,:], label='$PQ$')

# Mark points
coords = np.block([[P,Q,M]])
vert_labels = ['P','Q','M']
plt.scatter(coords[0,:], coords[1,:], color=['green','red','magenta'])
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points", xytext=(20,-10), ha='center')

# Axis styling
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.legend(loc='best')
plt.grid()
plt.axis('equal')

# Save figure as PDF
outfile_pdf = 'chapters/10/7/2/2/figs/fig.pdf'
plt.savefig(outfile_pdf)

# Save figure as PNG
outfile_png = 'chapters/10/7/2/2/figs/fig.png'
plt.savefig(outfile_png, dpi=300)

# Open image depending on system
try:
    import platform, subprocess, shlex
    if "termux" in platform.platform().lower():   # Android Termux
        subprocess.run(shlex.split(f"termux-open {outfile_png}"))
    else:                                        # Linux desktop
        subprocess.run(shlex.split(f"xdg-open {outfile_png}"))
except Exception as e:
    print(f"Could not auto-open file. Saved at {outfile_png}")
