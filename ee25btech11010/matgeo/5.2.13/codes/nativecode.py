import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(-5, 5, 400)

# Define equations
# Line 1: 2x - 2y = 2 -> y = x - 1
y1 = x - 1
label1 = r'$2x - 2y = 2$'

# Line 2: 4x - 4y = 5 -> y = x - 5/4
y2 = x - 1.25
label2 = r'$4x - 4y = 5$'

# --- Plot lines ---
plt.figure(figsize=(8,8))
line1, = plt.plot(x, y1, color='b')
line2, = plt.plot(x, y2, color='r')


x_coord_1 = 4
y_coord_1 = x_coord_1 - 1
plt.annotate(label1, 
             xy=(x_coord_1, y_coord_1), 
             xytext=(x_coord_1 + 0.2, y_coord_1 + 0.3),
            
             color='b',
             fontsize=12)

x_coord_2 = 4
y_coord_2 = x_coord_2 - 1.25
plt.annotate(label2, 
             xy=(x_coord_2, y_coord_2), 
             xytext=(x_coord_2 + 0.2, y_coord_2 - 0.5), 
             
             color='r',
             fontsize=12)

# --- Standard Plot Setup ---
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('System of Equations: Parallel Lines')
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/5.2.13/figs/q10.png")
plt.show()