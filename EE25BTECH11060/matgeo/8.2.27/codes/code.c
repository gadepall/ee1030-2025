#include <stdio.h>
// Function to compute V, u, f and print simplified equation
void conic_equation() {
    // Given parameters
    double e = 1;
    double c = 3;
    double F[2] = {0, -3};
    double n[2] = {0, 1};

    // Step 1: Compute V = ||n||^2 * I - e^2 * (n * n^T)
    double norm_n2 = n[0]*n[0] + n[1]*n[1];  // ||n||^2
    double V[2][2];

    V[0][0] = norm_n2 - e*e * n[0]*n[0];
    V[0][1] = 0 - e*e * n[0]*n[1];
    V[1][0] = 0 - e*e * n[1]*n[0];
    V[1][1] = norm_n2 - e*e * n[1]*n[1];

    // Step 2: Compute u = c*e^2*n - ||n||^2 * F
    double u[2];
    u[0] = c*e*e*n[0] - norm_n2*F[0];
    u[1] = c*e*e*n[1] - norm_n2*F[1];

    // Step 3: Compute f = ||n||^2 * ||F||^2 - c^2 * e^2
    double norm_F2 = F[0]*F[0] + F[1]*F[1];  // ||F||^2
    double f = norm_n2 * norm_F2 - c*c*e*e;

    // Step 4: Print results
    printf("V = [[%.2f, %.2f], [%.2f, %.2f]]\n", V[0][0], V[0][1], V[1][0], V[1][1]);
    printf("u = [%.2f, %.2f]\n", u[0], u[1]);
    printf("f = %.2f\n", f);
    printf("Simplified scalar equation: x^2 + 12*y = 0\n");
}
