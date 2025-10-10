#include <stdio.h>
#include <math.h>

int main() {
    // Given vectors
    double a[3] = {2, 3, -1};
    double b[3] = {1, -2, 1};
    double r[3], mag_r, unit_r[3], result[3];
    int i;

    // Calculate resultant r = a + b
    for(i = 0; i < 3; i++)
        r[i] = a[i] + b[i];

    // Magnitude of r
    mag_r = sqrt(r[0]*r[0] + r[1]*r[1] + r[2]*r[2]);

    // Unit vector in direction of r
    for(i = 0; i < 3; i++)
        unit_r[i] = r[i] / mag_r;

    // Vector of magnitude 5, parallel to r
    for(i = 0; i < 3; i++)
        result[i] = 5 * unit_r[i];

    // Print result
    printf("Vector of magnitude 5, parallel to resultant: ");
    printf("(%.4lf) i + (%.4lf) j + (%.4lf) k\n", result[0], result[1], result[2]);

    return 0;
}