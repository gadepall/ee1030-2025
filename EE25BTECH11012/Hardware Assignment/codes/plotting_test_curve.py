import numpy as np
import matplotlib.pyplot as plt

# --- Temperature vs Voltage Data ---
temp = np.array([44.9, 46.5, 48.2, 49.9, 51.8, 53.7, 84.7])
volt = np.array([1.838, 1.843, 1.848, 1.852, 1.857, 1.862, 1.920])

# Sort for smooth curve
sorted_idx = np.argsort(temp)
temp = temp[sorted_idx]
volt = volt[sorted_idx]

# Quadratic fit
coeffs = np.polyfit(temp, volt, 2)
poly = np.poly1d(coeffs)

# Smooth data for curve
temp_smooth = np.linspace(40, 90, 300)
volt_smooth = poly(temp_smooth)

# Plot
plt.figure(figsize=(8,6))
plt.plot(temp_smooth, volt_smooth, 'r-', linewidth=2, label='Curve')
plt.scatter(temp, volt, color='blue', s=50, label='Measured Data')

plt.xlabel("Temperature (°C)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs Temperature")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Scaling (like you asked)
plt.xlim(40, 90)
plt.ylim(1.83, 1.93)
plt.xticks(np.arange(40, 91, 5))
plt.yticks(np.arange(1.83, 1.94, 0.01))

plt.show()

# Print quadratic equation
print("Quadratic Fit Equation:")
print(f"Voltage = {coeffs[0]:.8f}*T² + {coeffs[1]:.8f}*T + {coeffs[2]:.8f}")