import ctypes
import math
import os
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled C shared library
if os.name == "nt":
    lib = ctypes.CDLL("./plane.dll")   # Windows
else:
    lib = ctypes.CDLL("./plane.so")    # Linux/macOS

# Function signatures
lib.dot.argtypes = [ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.c_int]
lib.dot.restype = ctypes.c_double

lib.compute_direction.argtypes = [ctypes.c_double,
                                  ctypes.c_double,
                                  ctypes.POINTER(ctypes.c_double)]
lib.compute_direction.restype = ctypes.c_double


def main():
    alpha = 30.0
    beta  = 120.0

    # allocate space for d[3]
    d = (ctypes.c_double * 3)()

    # Call C function to compute direction cosines
    lib.compute_direction(alpha, beta, d)

    # Convert to Python list
    d_vec = [d[i] for i in range(3)]

    # Print direction cosines
    print("Direction Cosines:")
    print(f"cos(alpha) = {d_vec[0]:.4f}")
    print(f"cos(beta)  = {d_vec[1]:.4f}")
    print(f"cos(gamma) = {d_vec[2]:.4f}")

    # Verify with dot product
    arr = (ctypes.c_double * 3)(*d_vec)
    check = lib.dot(arr, arr, 3)
    print(f"\nd^T d = {check:.4f} (should be 1)")

    # Angle with Z-axis
    gamma_deg = math.degrees(math.acos(d_vec[2]))
    print(f"The line makes an angle of {gamma_deg:.2f}° with the positive Z-axis.\n")

    # -------- Plotting Section --------
    os.makedirs("figs", exist_ok=True)

    d = np.array(d_vec)
    t = np.linspace(-3, 3, 100)
    x = d[0] * t
    y = d[1] * t
    z = d[2] * t

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the line
    ax.plot(x, y, z, color="blue", label=r"$L : (\cos\alpha, \cos\beta, \cos\gamma)t$")

    # Draw coordinate axes
    ax.quiver(0, 0, 0, 3, 0, 0, color="red", arrow_length_ratio=0.05)
    ax.text(3.2, 0, 0, "X", color="red")

    ax.quiver(0, 0, 0, 0, 3, 0, color="green", arrow_length_ratio=0.05)
    ax.text(0, 3.2, 0, "Y", color="green")

    ax.quiver(0, 0, 0, 0, 0, 3, color="black", arrow_length_ratio=0.05)
    ax.text(0, 0, 3.2, "Z", color="black")

    # Axis labels
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("Line with Direction Cosines (from C code)")

    ax.legend()

    # Set view limits
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    # Save and show
    plt.savefig("figs/ctypes_vector.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()