#include <stdio.h>
#include <math.h>

// Function to compute the area of a triangle given coordinates of points
double triangleArea(double Ax, double Ay, double Bx, double By, double Cx, double Cy) {
    double cross_product = (Ax - Bx) * (Ay - Cy) - (Ay - By) * (Ax - Cx);
    return 0.5 * fabs(cross_product);
}
