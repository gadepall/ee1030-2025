#include <stdio.h>
#include <math.h>

int main() {
    // Normal vector of the plane
    double n_x = 2.0, n_y = -3.0, n_z = 6.0;

    // Direction vector of x-axis
    double a_x = 1.0, a_y = 0.0, a_z = 0.0;

    // Dot product n · a
    double dot = n_x * a_x + n_y * a_y + n_z * a_z;

    // Magnitudes of n and a
    double mag_n = sqrt(n_x*n_x + n_y*n_y + n_z*n_z);
    double mag_a = sqrt(a_x*a_x + a_y*a_y + a_z*a_z);

    // Cos(theta) between normal and x-axis
    double cos_theta = dot / (mag_n * mag_a);

    // Alpha = cos(theta) since angle between plane and x-axis = 90° - theta
    double alpha = cos_theta;

    printf("The value of alpha = %lf\n", alpha);

    return 0;
}
