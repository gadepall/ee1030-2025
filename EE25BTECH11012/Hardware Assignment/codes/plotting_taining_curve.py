import matplotlib.pyplot as plt
import numpy as np

# --- 1. Data from the Image Table ---
temperature_data = np.array([33.9, 35.5, 48.5, 74.4, 80.8])
voltage_data = np.array([1.75, 1.80, 1.86, 1.89, 1.92])

# --- 2. Calculate the True Quadratic Best Fit ---
# Use np.polyfit to find the best-fit coefficients for a degree=2 polynomial.
# Coefficients will be [a2, a1, a0]
best_fit_coeffs = np.polyfit(temperature_data, voltage_data, deg=2)

# Create the polynomial function object
quadratic_model = np.poly1d(best_fit_coeffs)

# --- 3. Prepare the Curve Plotting Points ---
# Create a smooth range of x-values (Temperature) for the curve
# Use the actual data range for the plot line
T_range = np.linspace(temperature_data.min(), temperature_data.max(), 100)

# Calculate the corresponding y-values (Voltage) using the new best-fit model
V_curve = quadratic_model(T_range)


# --- 4. Plotting the Graph (Using the fixed X-label from last response) ---
plt.figure(figsize=(8, 6))

# Scatter Plot the Data Points
plt.scatter(
    temperature_data,
    voltage_data,
    color='red',
    marker='o',
    s=50,
    label='Data Points')

# Plot the True Best Fit Quadratic Curve
plt.plot(T_range,
    V_curve,
    color='blue',
    linestyle='-',
    linewidth=2,
    label='Quadratic Fit')

# --- 5. Customizing the Graph ---

# Using the recommended raw string fix for the degree symbol
plt.xlabel(r"Temperature (\u00B0C)", fontsize=12)
plt.ylabel("Voltage (V)", fontsize=12)
plt.title("Temperature vs. Voltage with True Quadratic Regression")

# Setting the Y-axis limits (as you requested)
plt.ylim(1.70, 2.00)

# Grid lines and legend for clarity
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig("Hardgraph.png")
plt.show()

# --- Optional: Print the calculated coefficients ---
print("\nCalculated Best-Fit Quadratic Model (V as a function of T):")
print(quadratic_model)