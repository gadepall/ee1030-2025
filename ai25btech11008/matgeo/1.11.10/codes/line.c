#include <stdio.h>
#include <math.h>

int main() {
    // Step 1: Define points P and Q
    double P[3] = {4, 3, -5};
    double Q[3] = {-2, 1, 8};

    // Step 2: Direction vector PQ = Q - P
    double PQ[3];
    PQ[0] = Q[0] - P[0];   // -6
    PQ[1] = Q[1] - P[1];   // -2
    PQ[2] = Q[2] - P[2];   // 13

    // Step 3: Magnitude of PQ
    double mag = sqrt(PQ[0]*PQ[0] + PQ[1]*PQ[1] + PQ[2]*PQ[2]);

    // Step 4: Direction cosines
    double cos_alpha = PQ[0] / mag;
    double cos_beta  = PQ[1] / mag;
    double cos_gamma = PQ[2] / mag;

    // Output
    printf("Vector PQ = (%.0f, %.0f, %.0f)\n", PQ[0], PQ[1], PQ[2]);
    printf("|PQ| = sqrt(209) = %.4f\n", mag);
    printf("Direction cosines:\n");
    printf("cos(alpha) = %.4f\n", cos_alpha);
    printf("cos(beta)  = %.4f\n", cos_beta);
    printf("cos(gamma) = %.4f\n", cos_gamma);

    return 0;
}

