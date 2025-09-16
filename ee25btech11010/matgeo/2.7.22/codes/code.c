#include <stdio.h>
#include <math.h>  // for fabs

// Function to compute area of a triangle given three vertices
double triangle_area(double x1, double y1,
                     double x2, double y2,
                     double x3, double y3)
{
    double area = fabs(x1 * (y2 - y3) +
                       x2 * (y3 - y1) +
                       x3 * (y1 - y2)) / 2.0;
    return area;
}

int main() {
    // Given vertices
    double x1 = 5, y1 = 0;
    double x2 = 8, y2 = 0;
    double x3 = 8, y3 = 4;

    double area = triangle_area(x1, y1, x2, y2, x3, y3);

    printf("The area of the triangle is: %.2f sq.units\n", area);

    return 0;
}
