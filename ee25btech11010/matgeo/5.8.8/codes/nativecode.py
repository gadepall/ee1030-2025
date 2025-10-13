import matplotlib.pyplot as plt
import numpy as np

# Define v2 range
v2 = np.linspace(0, 100, 200)

# Equations
v1_towards = 100 - v2      # v1 + v2 = 100
v1_same = 20 + v2          # v1 - v2 = 20

# Plot
plt.figure(figsize=(6,6))
plt.plot(v2, v1_towards, color='blue')
plt.plot(v2, v1_same, color='red')

# Intersection point
v2_meet = 40
v1_meet = 60
plt.plot(v2_meet, v1_meet, 'ko')  # solution point

# Annotate the lines
plt.text(60, 40, 'v1 + v2 = 100', color='blue')
plt.text(10, 35, 'v1 - v2 = 20', color='red')

# Annotate solution point
plt.text(v2_meet + 2, v1_meet, '(60, 40)', color='black')

plt.xlabel('v2 (km/h)')
plt.ylabel('v1 (km/h)')
plt.title('Graphical Solution of Speeds')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/5.8.8/figs/speed.png")
plt.show()
