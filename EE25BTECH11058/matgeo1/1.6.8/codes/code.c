#include <stdio.h>

int main() {

    double y1 = -1.0;
    double x2 = 2.0, y2 = 1.0;
    double x3 = 4.0, y3 = 5.0;
    double x1;
    double numerator = y1 * (x2 - x3) - (x2 * y3 - x3 * y2);

    double denominator = y2 - y3;

    x1 = numerator / denominator;

    printf("Using the matrix determinant method for collinear points:\n");
    printf("The value of x is: %.1f\n", x1);

return 0;
}