#include <stdio.h>
#include <math.h>

int main() {
    double Rx = 50.91;
    double Ry = -0.09;

    double dot_product = Rx * 1 + Ry * 0;  // dot with East vector [1, 0]
    double mag_R = sqrt(Rx * Rx + Ry * Ry);

    double cos_theta = dot_product / mag_R;
    double theta_rad = acos(cos_theta);
    double theta_deg = theta_rad * (180.0 / M_PI);

    printf("Angle from East = %.4f degrees\n", theta_deg);
    return 0;
}
