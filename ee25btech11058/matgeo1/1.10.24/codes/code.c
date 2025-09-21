#include <stdio.h>
#include <math.h>

int main() {
    // Plane equation: 6x - 3y - 2z + 1 = 0
    // Normal vector = (6, -3, -2)
    double a = 6, b = -3, c = -2;

    // Step 1: Print normal vector
    printf("Normal vector to the plane: (%.2f, %.2f, %.2f)\n", a, b, c);

    // Step 2: Find norm of the vector
    double norm = sqrt(a*a + b*b + c*c);
    printf("Norm of the vector = sqrt(%.2f^2 + %.2f^2 + %.2f^2) = %.2f\n", a, b, c, norm);

    // Step 3: Find unit vector
    double ux = a / norm;
    double uy = b / norm;
    double uz = c / norm;

    printf("Unit vector (u) = (%.2f, %.2f, %.2f)\n", ux, uy, uz);

    // Step 4: Direction cosines = components of unit vector
    printf("Direction cosines of the unit vector perpendicular to the plane:\n");
    printf("l = %.2f, m = %.2f, n = %.2f\n", ux, uy, uz);

    return 0;
}
