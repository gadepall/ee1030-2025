#include <stdio.h>
#include <math.h>

int main() {
    // Given values
    double mag_a = sqrt(3.0);   // |a|
    double mag_b = 4.0;         // |b|
    double dot_ab = 2 * sqrt(3.0); // a·b

    // Formula: cosθ = (a·b) / (|a||b|)
    double cos_theta = dot_ab / (mag_a * mag_b);

    // Find angle in radians
    double theta_rad = acos(cos_theta);

    // Convert to degrees
    double theta_deg = theta_rad * 180.0 / M_PI;

    printf("The angle between the two vectors is: %.2f degrees\n", theta_deg);

    return 0;
}
