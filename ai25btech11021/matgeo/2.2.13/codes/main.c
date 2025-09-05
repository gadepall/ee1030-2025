#include <stdio.h>
#include <math.h>

int main() {
    double dot_product = 2 * sqrt(3);
    double magnitude_a = sqrt(3);
    double magnitude_b = 4.0;

    double cos_theta = dot_product / (magnitude_a * magnitude_b);
    double theta_rad = acos(cos_theta);  // angle in radians
    double theta_deg = theta_rad * (180.0 / M_PI);  // convert to degrees

    printf("cos(theta) = %.6f\n", cos_theta);
    printf("Angle (in radians) = %.6f\n", theta_rad);
    printf("Angle (in degrees) = %.6f\n", theta_deg);

    return 0;
}
