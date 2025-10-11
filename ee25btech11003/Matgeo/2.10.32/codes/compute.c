#include <stdio.h>

// Function to compute R and S given vectors p and q
void computeRandS(double p[3], double q[3], double r[3], double s[3]) {
    // R = (3p + 2q) / 5
    for (int i = 0; i < 3; i++) {
        r[i] = (3 * p[i] + 2 * q[i]) / 5.0;
    }

    // S = 3p - 2q
    for (int i = 0; i < 3; i++) {
        s[i] = 3 * p[i] - 2 * q[i];
    }
}



