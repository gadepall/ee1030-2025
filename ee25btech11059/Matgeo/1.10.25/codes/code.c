#include <stdio.h>
#include <math.h>

#define DEG_TO_RAD(deg) ((deg) * (M_PI / 180.0))

int main() {
    // Define the angles in degrees
    double alpha = 90.0;  // Angle with X-axis
    double beta = 60.0;   // Angle with Y-axis
    double gamma = 30.0;  // Angle with Z-axis
    
    // Convert degrees to radians
    double alpha_rad = DEG_TO_RAD(alpha);
    double beta_rad = DEG_TO_RAD(beta);
    double gamma_rad = DEG_TO_RAD(gamma);

    // Calculate the direction cosines
    double l = cos(alpha_rad);  // cos(90 degrees)
    double m = cos(beta_rad);   // cos(60 degrees)
    double n = cos(gamma_rad);  // cos(30 degrees)

    // Print the direction cosines
    printf("Direction Cosines of the vector:\n");
    printf("l = cos(90 degrees) = %.2f\n", l);
    printf("m = cos(60 degrees) = %.2f\n", m);
    printf("n = cos(30 degrees) = %.2f\n", n);

    // Display the vector (l, m, n)
    printf("Direction cosines of vector x = (%.2f, %.2f, %.2f)\n", l, m, n);

    return 0;
}
