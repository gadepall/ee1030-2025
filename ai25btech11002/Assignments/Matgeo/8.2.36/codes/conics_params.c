#include <math.h>
#include <stdio.h>

// Helper: Euclidean norm
double norm2(const double *a, int n) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i)
        sum += a[i] * a[i];
    return sqrt(sum);
}

/*
 * Function: conpara
 * -----------------
 * Computes parabola parameters (V, u, f) given:
 *   F  : Focus (2D array)
 *   V0 : Vertex (2D array)
 *
 * Outputs:
 *   V  : 2×2 matrix (flattened)
 *   u  : 2D vector
 *   f  : scalar (via pointer)
 *
 * Relations:
 *   n = (V0 - F)/||V0 - F||
 *   c = nᵀV0 + ||V0 - F||   (sign = +1)
 *   V = I - n nᵀ
 *   u = c n - F
 *   f = ||F||² - c²
 */
void conpara(const double *F, const double *V0, double *V, double *u, double *f)
{
    // Step 1: Compute n = (V0 - F)/||V0 - F||
    double n_vec[2];
    n_vec[0] = V0[0] - F[0];
    n_vec[1] = V0[1] - F[1];

    double mag = norm2(n_vec, 2);
    n_vec[0] /= mag;
    n_vec[1] /= mag;

    // Step 2: Choose sign = +1
    int sign = 1;

    // Step 3: c = nᵀV0 + sign * ||V0 - F||
    double c = n_vec[0]*V0[0] + n_vec[1]*V0[1] + sign*mag;

    // Step 4: V = I - n nᵀ
    V[0] = 1 - n_vec[0]*n_vec[0];
    V[1] = -n_vec[0]*n_vec[1];
    V[2] = -n_vec[1]*n_vec[0];
    V[3] = 1 - n_vec[1]*n_vec[1];

    // Step 5: u = c n - F
    u[0] = c*n_vec[0] - F[0];
    u[1] = c*n_vec[1] - F[1];

    // Step 6: f = ||F||² - c²
    *f = (F[0]*F[0] + F[1]*F[1]) - c*c;
}

