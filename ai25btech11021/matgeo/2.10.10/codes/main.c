#include <stdio.h>

int main() {
    // Given vectors a and c
    double a[3] = {1, 1, 1};
    double c[3] = {0, 1, -1};

    // Variables for b components
    double x, y, z;

    // From the solution:
    // z = y
    // y = x - 1
    // x + y + z = 3  =>  x + (x-1) + (x-1) = 3  => 3x - 2 = 3  => x = 5/3

    x = 5.0 / 3.0;
    y = x - 1.0;
    z = y;

    // Print result
    printf("Vector b is:\n");
    printf("b = [%.6f, %.6f, %.6f]\n", x, y, z);

    return 0;
}
