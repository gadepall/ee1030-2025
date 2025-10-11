import numpy as np
import matplotlib.pyplot as plt

# Input sequence
x = np.array([1, 0, 2, 3])
N = len(x)
n = np.arange(N)

# DFT
X = np.fft.fft(x)
k = np.arange(N)

# --- Plot time-domain sequence ---
plt.figure()
plt.stem(n, x, basefmt=" ")
plt.title("Time-domain sequence x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.savefig("fig3.png")
plt.show()

# --- Plot magnitude spectrum ---
plt.figure()
plt.stem(k, np.abs(X), basefmt=" ")
plt.title("Magnitude spectrum |X[k]|")
plt.xlabel("k (frequency index)")
plt.ylabel("|X[k]|")
plt.savefig("fig4.png")
plt.show()

# --- Plot phase spectrum ---
plt.figure()
plt.stem(k, np.angle(X), basefmt=" ")
plt.title("Phase spectrum ∠X[k] (radians)")
plt.xlabel("k (frequency index)")
plt.ylabel("Phase [rad]")
plt.savefig("fig5.png")
plt.show()


