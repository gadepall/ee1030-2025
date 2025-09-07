#include <stdio.h>
#include <math.h>

int main() {
    double horizontal = 10.0;
    double vertical = 30.0;
    double theta_rad = atan(horizontal / vertical);
    double theta_deg = theta_rad * 180.0 / M_PI;

    printf("Horizontal component (north) = %.1f m/s,\n", horizontal);
    printf("Vertical component (down) = %.1f m/s.\n\n", vertical);
    printf("tan(theta) = %.1f / %.1f = %.2f\n", horizontal, vertical, horizontal / vertical);
    printf("theta = arctan(%.2f) ≈ %.2f degrees\n\n", horizontal / vertical, theta_deg);
    printf("Conclusion: In her frame the rain comes from slightly ahead (from the south and above),\n");
    printf("so she should tilt the umbrella forward (toward the direction of motion, i.e., south)\n");
    printf("by %.2f degrees from the vertical.\n", theta_deg);

    return 0;
}
