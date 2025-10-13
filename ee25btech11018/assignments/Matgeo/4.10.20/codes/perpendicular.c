#include <stdio.h>

// Function to calculate midpoint of AB
void midpoint(float Ax, float Ay, float Bx, float By, float *Mx, float *My) {
    *Mx = (Ax + Bx) / 2.0;
    *My = (Ay + By) / 2.0;
}

// Function to calculate direction vector (B - A)
void direction(float Ax, float Ay, float Bx, float By, float *dx, float *dy) {
    *dx = Bx - Ax;
    *dy = By - Ay;
}

// Function to calculate perpendicular bisector equation coefficients
// Returns c value; coeff[0] = a, coeff[1] = b
float perpendicularBisector(float Ax, float Ay, float Bx, float By, float coeff[2]) {
    float Mx, My, dx, dy;

    midpoint(Ax, Ay, Bx, By, &Mx, &My);
    direction(Ax, Ay, Bx, By, &dx, &dy);

    coeff[0] = dx;
    coeff[1] = dy;

    return (coeff[0] * Mx + coeff[1] * My);
}

// Function to find intersection with y-axis (x = 0)
float intersectionY(float coeff[2], float c) {
    // Equation: a*0 + b*y = c → y = c/b
    return c / coeff[1];
}


