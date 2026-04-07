import numpy as np
import matplotlib.pyplot as plt

# 1. Define the PMF
faces = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.array([1/4, 1/8, 1/8, 1/8, 1/8, 1/4])

# 2. Plot the PMF
plt.figure(figsize=(8, 5))
plt.stem(faces, probabilities, basefmt=" ")
plt.title("Probability Mass Function (PMF) of Loaded Die")
plt.xlabel("Die Value")
plt.ylabel("Probability")
plt.xticks(faces)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 3. Numerical Computation (Monte Carlo Simulation)
num_simulations = 1_000_000
# Roll 3 dice simultaneously for each simulation
rolls = np.random.choice(faces, size=(num_simulations, 3), p=probabilities)

# Check for specific sequence (1, 5, 6)
successes = np.all(rolls == [1, 5, 6], axis=1)
numerical_prob = np.mean(successes)

print(f"Theoretical Probability (1, 5, 6): {1/128:.6f}")
print(f"Numerical Probability (1, 5, 6):   {numerical_prob:.6f}")