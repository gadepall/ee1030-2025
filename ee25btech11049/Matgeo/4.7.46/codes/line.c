#include <math.h>
#include <stdio.h>

/*
 * Calculates the normal vectors of the two lines passing through a point P(px, py)
 * at a given distance 'd' from the origin using eigenvalue decomposition.
 *
 * The problem is defined by the matrix equation: n^T * M * n = 0
 * where M = P*P^T - d^2*I. The vectors 'n' that solve this are the desired normals.
 *
 * This function implements a direct matrix theory solution:
 * 1.  It constructs the symmetric matrix M.
 * 2.  It calculates the eigenvalues (lambda1, lambda2) and corresponding
 * eigenvectors (v1, v2) of M.
 * 3.  The solution vectors 'n' are shown to be linear combinations of the
 * eigenvectors:
 * n = sqrt(-lambda2) * v1  +/-  sqrt(lambda1) * v2
 * (up to a scaling factor, and assuming lambda1 > 0, lambda2 < 0).
 * 4.  These combinations are computed to find the final normals.
 *
 * @param px The x-coordinate of the point on the lines.
 * @param py The y-coordinate of the point on the lines.
 * @param d  The perpendicular distance of the lines from the origin.
 * @param out_a1 Pointer to store the 'a' component of the first normal vector.
 * @param out_b1 Pointer to store the 'b' component of the first normal vector.
 * @param out_a2 Pointer to store the 'a' component of the second normal vector.
 * @param out_b2 Pointer to store the 'b' component of the second normal vector.
 * @return 0 on success, -1 on failure (no real solution).
 */
int calculate_line_normals(double px, double py, double d,
                           double* out_a1, double* out_b1,
                           double* out_a2, double* out_b2) {

    // 1. Construct the symmetric matrix M = P*P^T - d^2*I
    double M11 = px*px - d*d;
    double M12 = px*py;
    double M22 = py*py - d*d;

    // 2. Find the eigenvalues of M by solving the characteristic equation:
    //    lambda^2 - trace(M)*lambda + det(M) = 0
    double trace = M11 + M22;
    double det = M11 * M22 - M12 * M12;

    double discriminant_lambda = trace*trace - 4*det;
    if (discriminant_lambda < 0) {
        // This should not happen for a real symmetric matrix
        return -1;
    }
    double sqrt_discriminant_lambda = sqrt(discriminant_lambda);
    double lambda1 = (trace + sqrt_discriminant_lambda) / 2.0; // Larger eigenvalue
    double lambda2 = (trace - sqrt_discriminant_lambda) / 2.0; // Smaller eigenvalue

    // 3. Check for real solutions. If det > 0, eigenvalues have the same sign.
    //    This means -lambda2/lambda1 is negative, leading to no real solution.
    //    This corresponds to the point P being inside the circle of radius d.
    if (det > 0.0) {
        return -1; // No real lines exist
    }

    // 4. Find the (non-normalized) eigenvector v1 for lambda1
    double v1_x = M12;
    double v1_y = lambda1 - M11;
    // Normalize v1
    double norm_v1 = sqrt(v1_x*v1_x + v1_y*v1_y);
    if (norm_v1 < 1e-9) { // Handle case where eigenvector is zero (M is diagonal)
        v1_x = 1.0; v1_y = 0.0; // A valid eigenvector
    } else {
        v1_x /= norm_v1; v1_y /= norm_v1;
    }


    // 5. Find the (non-normalized) eigenvector v2 for lambda2. Since M is
    //    symmetric, v2 is orthogonal to v1.
    double v2_x = -v1_y;
    double v2_y = v1_x;

    // 6. The solution vectors (our normals) are a specific linear combination
    //    of the normalized eigenvectors.
    double sqrt_l1 = sqrt(lambda1);
    double sqrt_neg_l2 = sqrt(-lambda2);

    double n1_x = sqrt_neg_l2 * v1_x + sqrt_l1 * v2_x;
    double n1_y = sqrt_neg_l2 * v1_y + sqrt_l1 * v2_y;
    
    double n2_x = sqrt_neg_l2 * v1_x - sqrt_l1 * v2_x;
    double n2_y = sqrt_neg_l2 * v1_y - sqrt_l1 * v2_y;

    // 7. Set the output values.
    *out_a1 = n1_x;
    *out_b1 = n1_y;
    *out_a2 = n2_x;
    *out_b2 = n2_y;

    return 0; // Success
}


