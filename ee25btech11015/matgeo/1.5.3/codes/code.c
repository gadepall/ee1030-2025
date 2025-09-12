#include <stdio.h>

// Function to compute ratio in which X-axis divides AB
// Returns ratio m:n as a floating point (m/n)
float find_ratio(float Ax, float Ay, float Bx, float By) {
    // Equation of line AB: y = slope * x + c
    float slope = (By - Ay) / (Bx - Ax);
    float intercept = Ay - slope * Ax;

    // Intersection with X-axis (y = 0)
    float x_intersect = -intercept / slope;
    float y_intersect = 0;

    // Compute distances AX and XB (only x-difference since y=0 for X)
    float AX = (Ax - x_intersect);
    if (AX < 0) AX = -AX;

    float XB = (Bx - x_intersect);
    if (XB < 0) XB = -XB;

    // Print ratio
    printf("The X-axis divides AB in the ratio %.0f:%.0f\n", AX, XB);

    // Return the floating ratio (AX/XB)
    return AX / XB;
}