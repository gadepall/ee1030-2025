#include <math.h>
void find_eigenvalues_2x2(double a, double b, double c, double d, double* eig1, double* eig2) {
    double trace = a + d;
    double determinant = a * d - b * c;
    double discriminant = trace * trace - 4 * determinant;
    
    if (discriminant >= 0) {
        double sqrt_discriminant = sqrt(discriminant);
        *eig1 = (trace + sqrt_discriminant) / 2.0;
        *eig2 = (trace - sqrt_discriminant) / 2.0;
    }
}
