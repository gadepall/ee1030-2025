#include <stdio.h>
#include <math.h>

// Function to compute intersection point Q
// Inputs: Px, Py = point P
// Outputs: Qx, Qy (via pointers)
void find_intersection(double Px, double Py, double *Qx, double *Qy) {
    // direction vector for 135° = (-1, 1)
    double dx = -1.0, dy = 1.0;

    // Parametric line: (x,y) = (Px + t dx, Py + t dy)
    // Line: 4x - y = 0  -> y = 4x
    // Substitute: Py + t dy = 4(Px + t dx)
    // => Py + t = 4Px + 4t dx
    // => Py + t = 4Px + 4t(-1)
    // => Py + t = 4Px - 4t
    // => t + 4t = 4Px - Py
    // => 5t = 4Px - Py
    double t = (4*Px - Py) / 5.0;

    *Qx = Px + t*dx;
    *Qy = Py + t*dy;
}

// Function to compute distance between two points
double distance(double x1, double y1, double x2, double y2) {
    return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

