#include <stdio.h>

int main() {
    // Components of the normal vector n = (a, b, c)
    int a, b, c;
    
    // Coordinates of the foot of the perpendicular F = (x0, y0, z0)
    int x0, y0, z0;

    // Input normal vector components
    printf("Enter normal vector components (a, b, c): ");
    scanf("%d %d %d", &a, &b, &c);

    // Input coordinates of foot of perpendicular
    printf("Enter foot of perpendicular coordinates (x0, y0, z0): ");
    scanf("%d %d %d", &x0, &y0, &z0);

    // Calculate d = a*x0 + b*y0 + c*z0
    int d = a * x0 + b * y0 + c * z0;

    // Print the plane equation
    printf("Equation of the plane: %dx + %dy + %dz = %d\n", a, b, c, d);

    return 0;
}
