import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the compiled library
quadrant_check = ctypes.CDLL('./func.so')
quadrant_check.check_quadrant.argtypes = [ctypes.c_double, ctypes.c_double]
quadrant_check.check_quadrant.restype = ctypes.c_char_p

def main():
    # Define the points ONCE
    points = [(-2, 4), (3, -1), (-1, 0),(1, 2), (-3, -5)]
    
    # Check each point using the C function
    print("Point Locations:")
    print("=" * 40)
    
    for i, (x, y) in enumerate(points):
        result_bytes = quadrant_check.check_quadrant(x, y)
        result = result_bytes.decode('utf-8')
        print(f"Point {i+1}: ({x}, {y}) -> {result}")
    print("=" * 40)
    
    plt.figure(figsize=(8, 8))
    plt.axhline(0, color='black')  # x-axis
    plt.axvline(0, color='black')  # y-axis

    for (x, y) in points:
        plt.scatter(x, y, s=80)
        plt.text(x+0.1, y+0.1, f"({x},{y})", fontsize=9)

    plt.title("Points on Cartesian Plane (Q1.2.19)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig("/home/gauthamp/ee1030-2025/ai25btech11013/matgeo/1.2.19/figs/plotc.png")
    plt.show()


