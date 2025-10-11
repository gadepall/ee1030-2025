#include <stdio.h>
#include <stdlib.h>

int main() {
    // Coordinates of the triangle
    int x1 = 1, y1 = 0;
    int x2 = 2, y2 = 2;
    int x3 = 3, y3 = 1;

    // Applying formula
    int determinant = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2);
    float area = 0.5 * abs(determinant);

    printf("Area of the triangle = %.2f\n", area);

    return 0;
}
