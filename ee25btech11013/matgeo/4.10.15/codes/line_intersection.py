import numpy as np
import matplotlib.pyplot as plt
import ctypes


lib = ctypes.CDLL("./line_intersection.so")


lib.line_intersection.argtypes = [
    np.ctypeslib.ndpointer(ctypes.c_double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(ctypes.c_double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(ctypes.c_double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(ctypes.c_double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(ctypes.c_double, ndim=1, flags="C_CONTIGUOUS"),
]
lib.line_intersection.restype = ctypes.c_int


p1, d1 = np.array([1.0, 2.0, 3.0]), np.array([2.0, 3.0, 4.0])
p2, d2 = np.array([4.0, 1.0, 0.0]), np.array([5.0, 2.0, 1.0])
intersection = np.zeros(3, dtype=np.float64)


status = lib.line_intersection(p1, d1, p2, d2, intersection)
if status != 0:
    print("The lines are parallel or skew; no intersection.")
else:
    print(f"The lines intersect at: {intersection.astype(int)}")


    eq1 = f"L1: (x,y,z) = ({int(p1[0])},{int(p1[1])},{int(p1[2])}) + t({int(d1[0])},{int(d1[1])},{int(d1[2])})"
    eq2 = f"L2: (x,y,z) = ({int(p2[0])},{int(p2[1])},{int(p2[2])}) + t({int(d2[0])},{int(d2[1])},{int(d2[2])})"


    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    t = np.linspace(-2, 2, 50)
    line1_points = p1 + t[:, None] * d1
    line2_points = p2 + t[:, None] * d2

    ax.plot(line1_points[:, 0], line1_points[:, 1], line1_points[:, 2], label=eq1)
    ax.plot(line2_points[:, 0], line2_points[:, 1], line2_points[:, 2], label=eq2)

    ax.scatter(intersection[0], intersection[1], intersection[2],
               color="red", s=100, zorder=5, label=f"Intersection {intersection.astype(int)}")
    ax.text(intersection[0], intersection[1], intersection[2],
            f"{intersection.astype(int)}", color="red", fontsize=10)

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title("Intersection of Two Lines in 3D")
    ax.legend()
    plt.savefig('/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/4.10.15/figs/Figure_1.png')
    plt.show()
