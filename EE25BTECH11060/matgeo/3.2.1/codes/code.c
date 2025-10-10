#include <stdio.h>
#include <math.h>

int main() {
    // Given lengths
    double AB = 4.0, BC = 6.0, AC = 9.0;

    // Assign coordinates for A and B
    double Ax = 0, Ay = 0;
    double Bx = 4, By = 0;

    // Using cosine rule to find cos(A)
    double cosA = (AB*AB + AC*AC - BC*BC) / (2 * AB * AC);
     double sinA = sqrt(1 - cosA*cosA);
    

    // Coordinates of C
    double Cx = Ax + AC * cosA;
    double Cy = Ay + AC * sinA;

    // Print results
    printf("Coordinates of A: (%.2f, %.2f)\n", Ax, Ay);
    printf("Coordinates of B: (%.2f, %.2f)\n", Bx, By);
    printf("Coordinates of C: (%.2f, %.2f)\n", Cx, Cy);

    return 0;
}
