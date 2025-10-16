#include <math.h>

void find_2x2_eigenvalues(double a, double b, double c, double d,
                                double* eig1_real, double* eig1_imag,
                                double* eig2_real, double* eig2_imag) {
    double trace = a + d;
    double determinant = a * d - b * c;
    double discriminant = trace * trace - 4 * determinant;

    if (discriminant >= 0) {
        // Real eigenvalues
        double sqrt_discriminant = sqrt(discriminant);
        *eig1_real = (trace + sqrt_discriminant) / 2.0;
        *eig1_imag = 0.0;
        *eig2_real = (trace - sqrt_discriminant) / 2.0;
        *eig2_imag = 0.0;
    } else {
        // Complex conjugate eigenvalues
        double sqrt_abs_discriminant = sqrt(-discriminant);
        *eig1_real = trace / 2.0;
        *eig1_imag = sqrt_abs_discriminant / 2.0;
        *eig2_real = trace / 2.0;
        *eig2_imag = -sqrt_abs_discriminant / 2.0;
    }
}
