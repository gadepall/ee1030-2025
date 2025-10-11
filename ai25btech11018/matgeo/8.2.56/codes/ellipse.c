#include <stdio.h>
#include <math.h>

int main() {
    // --- Step 1: Represent the Ellipse in Matrix Form ---
    // The equation is 9x^2 + 25y^2 = 225
    // In matrix form: x^T * V * x + 2u^T * x + f = 0
    // V = [[9, 0], [0, 25]]
    // u = [0, 0]
    // f = -225

    double V[2][2] = {{9.0, 0.0}, {0.0, 25.0}};
    double u[2] = {0.0, 0.0};
    double f = -225.0;

    // --- Step 2: Find the Eccentricity ---
    // The eigenvalues of V are the diagonal elements.
    double lambda1 = V[0][0]; // 9
    double lambda2 = V[1][1]; // 25

    // The eccentricity formula is e = sqrt(1 - lambda1/lambda2)
    double eccentricity = sqrt(1.0 - (lambda1 / lambda2));

    printf("The eccentricity of the ellipse is: %.2f\n\n", eccentricity);

    // --- Step 3: Find the Foci ---
    // The center is c = -V^-1 * u. Since u is the zero vector, the center is at (0, 0).
    double center_x = 0.0;
    double center_y = 0.0;

    // The major axis length is 2*a, where a = sqrt(f0 / |lambda_min|)
    // f0 = u^T*V^-1*u - f = 0 - f = -f
    double f0 = -f; // 225

    // The semi-major axis 'a' corresponds to the smaller eigenvalue (9).
    double semi_major_axis = sqrt(f0 / lambda1); // sqrt(225/9) = sqrt(25) = 5
    
    // The distance from the center to each focus is 'ae'
    double foci_distance = semi_major_axis * eccentricity;

    // The foci are located on the major axis (the x-axis, corresponding to lambda1)
    printf("The foci are located at (+/- ae, 0):\n");
    printf("Foci: (%.2f, %.2f) and (%.2f, %.2f)\n", foci_distance, 0.0, -foci_distance, 0.0);

    return 0;
}