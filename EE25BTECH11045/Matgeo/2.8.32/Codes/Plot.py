import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Coordinates
H = (2, 4)
B = (5, 8)
S = (13, 14)
O = (13, 26)

# Path via B & S
x_via = [H[0], B[0], S[0], O[0]]
y_via = [H[1], B[1], S[1], O[1]]

# Direct Path
x_direct = [H[0], O[0]]
y_direct = [H[1], O[1]]

plt.figure(figsize=(6,6))
# Plot via B & S (blue path)
plt.plot(x_via, y_via, 'bo-', label="Via B & S")

# Plot direct path (green dashed)
plt.plot(x_direct, y_direct, 'g--', label="Direct Path")

# Label points
for point, name in zip([H, B, S, O], ['H', 'B', 'S', 'O']):
    plt.text(point[0]+0.3, point[1], f"{name} {point}", fontsize=10)

# Labels
plt.xlabel("X Coordinate (km)")
plt.ylabel("Y Coordinate (km)")
plt.title("Paths between H and O")
plt.legend()
plt.grid(True)

plt.show()