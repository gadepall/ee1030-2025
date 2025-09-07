import ctypes
import matplotlib.pyplot as plt
import numpy as np

lib = ctypes.CDLL('/storage/self/primary/Matrix/ee1030-2025/ee25btech11035/Assignments/matgeo/1.9.24/codes/1.so')

lib.findk.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.findk.restype = ctypes.c_float

qx, qy = 2, -5
rx, ry = -3, 6

print(f"Point Q: ({qx}, {qy})")
print(f"Point R: ({rx}, {ry})")

k = lib.findk(qx, qy, rx, ry)
print(f"Calculated k: {k}")

px = 2 * k
py = k
print(f"Point P: ({px}, {py})")

plt.figure(figsize=(10, 8))

plt.scatter(qx, qy, color='red', s=100, label=f'Q({qx}, {qy})', zorder=5)
plt.scatter(rx, ry, color='blue', s=100, label=f'R({rx}, {ry})', zorder=5)
plt.scatter(px, py, color='green', s=100, label=f'P({px:.2f}, {py:.2f})', zorder=5)

plt.annotate('Q', (qx, qy), xytext=(5, 5), textcoords='offset points', fontsize=12, fontweight='bold')
plt.annotate('R', (rx, ry), xytext=(5, 5), textcoords='offset points', fontsize=12, fontweight='bold')
plt.annotate('P', (px, py), xytext=(5, 5), textcoords='offset points', fontsize=12, fontweight='bold')

plt.plot([qx, rx], [qy, ry], 'k--', alpha=0.5, linewidth=1, label='QR')
plt.plot([qx, px], [qy, py], 'g--', alpha=0.5, linewidth=1, label='QP')
plt.plot([rx, px], [ry, py], 'g--', alpha=0.5, linewidth=1, label='RP')

plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Points Q, R, and P plotted')
plt.legend()

plt.axis('equal')

all_x = [qx, rx, px]
all_y = [qy, ry, py]
x_margin = (max(all_x) - min(all_x)) * 0.1
y_margin = (max(all_y) - min(all_y)) * 0.1
plt.xlim(min(all_x) - x_margin - 1, max(all_x) + x_margin + 1)
plt.ylim(min(all_y) - y_margin - 1, max(all_y) + y_margin + 1)

plt.tight_layout()
plt.savefig('1.png')
plt.show()

print("\n" + "="*50)
print("SUMMARY:")
print("="*50)
print(f"Input points: Q({qx}, {qy}), R({rx}, {ry})")
print(f"Calculated k value: {k:.6f}")
print(f"Resulting point P: ({px:.6f}, {py:.6f})")
print("="*50)
