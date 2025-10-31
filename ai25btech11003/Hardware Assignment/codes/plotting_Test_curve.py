#CODE BY BHAVESH G & SUJAL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading your data
df = pd.read_csv("../data/test.csv")
T = df["T"].values
V = df["V"].values


#Just Printing Best Fit Curve.
df2 = pd.read_csv("../data/train.csv")
T2 = df2["T"].values
V2 = df2["V"].values
# V = a*T^2 + b*T + c
coeffs = np.polyfit(T2, V2, 2)
a, b, c = coeffs
print(f"Best-fit curve: V = {a:.6e}·T² + {b:.6e}·T + {c:.6e}")

#Computing fitted values for plotting
T_sorted = np.linspace(T.min(), T.max(), 200)
V_fit = np.polyval(coeffs, T_sorted)

#Ticks
x_ticks = np.arange(34,90, 2)

#Plotting the raw data and the best‑fit curve
plt.figure(figsize=(8,5))
plt.scatter(T, V, color="000", zorder=5, marker="H", s=50, label="Measured Data")
plt.plot(T_sorted, V_fit, lw=3, label="Best-fitted curve")

#Labelling and Adjusting Axises
plt.xlabel("Temperature (°C)", fontsize=25)
plt.ylabel("Output Voltage (V)", fontsize=25)
plt.xticks(x_ticks)

#Anonymous Attributes
plt.legend()
plt.grid(True)
plt.tight_layout()

#Saving and Showing the Images
plt.savefig("../figs/fig2.png", dpi=300)
plt.show()
