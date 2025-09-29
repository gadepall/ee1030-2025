#include <stdio.h>
#include <math.h>  // For fabs()

// Function to calculate the 2D cross product of vectors u and v
double crossProduct(double u1, double u2, double v1, double v2) {
    return u1 * v2 - u2 * v1;
}

int main() {
    // Coordinates of points A, B, C
    double Ax = 1, Ay = -1;
    double Bx = -4, By = 6;
    double Cx = -3, Cy = 5;

    // Calculate vectors A-B and B-C
    double ABx = Ax - Bx;
    double ABy = Ay - By;
    double BCx = Bx - Cx;
    double BCy = By - Cy;

    // Calculate the cross product magnitude
    double cross = crossProduct(ABx, ABy, BCx, BCy);

    // Calculate area = 1/2 * |cross product|
    double area = 0.5 * fabs(cross);

    printf("Area of triangle ABC = %.2f square units\n", area);

    return 0;
}
