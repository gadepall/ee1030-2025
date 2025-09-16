#include <stdio.h>
#include <math.h>

// Function to compute area of triangle from 3 points
double triangle_area(double x1, double y1, double x2, double y2, double x3, double y3) {
    double det = x1*(y2 - y3) - y1*(x2 - x3) + (x2*y3 - y2*x3);
    return fabs(det) / 2.0;
}

int main() {
    double A[2] = {2, 5};
    double B[2] = {4, 7};
    double C[2] = {6, 2};

    double area = triangle_area(A[0], A[1], B[0], B[1], C[0], C[1]);
    printf("Area of triangle ABC = %.2f\n", area);
    return 0;
}
