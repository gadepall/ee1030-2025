#include <math.h>

/*
 * Calculates the eigenvalues and normalized eigenvectors for a 2x2 real matrix.
 * Matrix is [[a, b], [c, d]].
 *
 * Output pointers store the results:
 * eig_val1, eig_val2: The two eigenvalues.
 * eig_vec1_x, eig_vec1_y: The components of the first eigenvector.
 * eig_vec2_x, eig_vec2_y: The components of the second eigenvector.
*/
void find_eigen_system_2x2(
    double a, double b, double c, double d,
    double* eig_val1, double* eig_val2,
    double* eig_vec1_x, double* eig_vec1_y,
    double* eig_vec2_x, double* eig_vec2_y) {

    // --- Find Eigenvalues ---
    double trace = a + d;
    double determinant = (a * d) - (b * c);
    double discriminant = sqrt(trace * trace - 4 * determinant);

    *eig_val1 = (trace + discriminant) / 2.0;
    *eig_val2 = (trace - discriminant) / 2.0;

    // --- Find Eigenvector for eig_val1 ---
    double v1x = b;
    double v1y = *eig_val1 - a;
    double mag1 = sqrt(v1x * v1x + v1y * v1y);
    // Avoid division by zero for diagonal matrices where b=0
    if (mag1 < 1e-9) {
        *eig_vec1_x = 1.0;
        *eig_vec1_y = 0.0;
    } else {
        *eig_vec1_x = v1x / mag1;
        *eig_vec1_y = v1y / mag1;
    }


    // --- Find Eigenvector for eig_val2 ---
    double v2x = b;
    double v2y = *eig_val2 - a;
    double mag2 = sqrt(v2x * v2x + v2y * v2y);
    // Avoid division by zero
    if (mag2 < 1e-9) {
        *eig_vec2_x = 0.0;
        *eig_vec2_y = 1.0;
    } else {
        *eig_vec2_x = v2x / mag2;
        *eig_vec2_y = v2y / mag2;
    }
}