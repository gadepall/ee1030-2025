#include <math.h>


void calculate_eigenvalues(double *matrix, double *eigenvalues) {
    // Extract matrix elements
    double a = matrix[0];
    double b = matrix[1];
    double c = matrix[2];
    double d = matrix[3];

    // Calculate trace and determinant
    double trace = a + d;
    double determinant = a * d - b * c;

    // Calculate the discriminant of the characteristic equation
    double discriminant = trace * trace - 4 * determinant;

    if (discriminant >= 0) {
        double sqrt_discriminant = sqrt(discriminant);
        eigenvalues[0] = (trace + sqrt_discriminant) / 2.0;
        eigenvalues[1] = (trace - sqrt_discriminant) / 2.0;
    } else {
        // Handle case for complex eigenvalues if necessary
        eigenvalues[0] = NAN;
        eigenvalues[1] = NAN;
    }
}

