#include <stdio.h>
#include <math.h>

int main() {
    // Given values
    double BC = 6.0;
    double AB = 5.0;
    double angle_ABC = 60.0; // in degrees

    // Convert degrees to radians
    double angle_rad = angle_ABC * M_PI / 180.0;

    // Apply cosine rule: AC^2 = AB^2 + BC^2 - 2*AB*BC*cos(angle)
    double AC = sqrt(AB*AB + BC*BC - 2*AB*BC*cos(angle_rad));

    // Print results
    printf("Given: BC = %.2f cm, AB = %.2f cm, Angle ABC = %.2f degrees\n", BC, AB, angle_ABC);
    printf("The length of AC = %.2f cm\n", AC);

    return 0;
}
