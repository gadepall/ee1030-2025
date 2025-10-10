from ctypes import CDLL
import matplotlib.pyplot as plt

# load shared library
lib = CDLL("./libparallelogram.so")

# run C main program to generate coords.dat
import os
os.system("./main")

# read coords
coords = []
with open("coords.dat") as f:
    for line in f:
        x,y = map(int,line.split())
        coords.append((x,y))

# close polygon
coords.append(coords[0])

# plot
xs, ys = zip(*coords)
plt.plot(xs, ys, marker='o')
plt.text(1,3,"A(1,3)")
plt.text(-1,2,"B(-1,2)")
plt.text(0,4,"D(0,4)")
plt.text(2,5,"C(2,5)")
plt.title("Parallelogram ABCD")
plt.grid(True)
plt.savefig("/home/r-nikhil/ee1030-2025/ai25btech11025/matgeo/1.3.4/figs/plotc.png")
plt.show()

