import math

# Coordinates of points P and Q
Px, Py, Pz = 4, 3, -5
Qx, Qy, Qz = -2, 1, -8

# Direction vector PQ = Q - P
dx = Qx - Px
dy = Qy - Py
dz = Qz - Pz

# Magnitude of PQ
magnitude = math.sqrt(dx**2 + dy**2 + dz**2)

# Direction cosines (unit vector components)
l = dx / magnitude
m = dy / magnitude
n = dz / magnitude

# Output the result
print(f"Direction Cosines: ({l:.3f}, {m:.3f}, {n:.3f})")

