import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function T(s) = (s - 5) / (s^2 + 5s + 6)
num = [1, -5]
den = [1, 5, 6]
sys = signal.TransferFunction(num, den)

# 1. Pole-Zero Map
zeros = np.roots(num)
poles = np.roots(den)

plt.figure(figsize=(6, 5))
plt.scatter(poles.real, poles.imag, marker='x', color='red', s=100, label='Poles (at -2, -3)')
plt.scatter(zeros.real, zeros.imag, marker='o', edgecolors='blue', facecolors='none', s=100, label='Zero (at +5)')
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--')
plt.title('Pole-Zero Map (Showing RHP Zero)')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()
plt.show()

# 2. Step Response (Demonstrates Stability and Undershoot)
t, y = signal.step(sys)
plt.figure(figsize=(8, 4))
plt.plot(t, y, 'b', label='Step Response')
plt.axhline(0, color='black', lw=1)
plt.title('Step Response (Notice the initial "Undershoot")')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()

# 3. Bode Plot
w, mag, phase = signal.bode(sys)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
ax1.semilogx(w, mag)
ax1.set_title('Bode Plot')
ax1.set_ylabel('Magnitude (dB)')
ax1.grid(True)

ax2.semilogx(w, phase)
ax2.set_ylabel('Phase (degrees)')
ax2.set_xlabel('Frequency (rad/s)')
ax2.grid(True)
plt.show()