#include <stdio.h>
#include <math.h>

// Function to compute dot product
double dot(double* a, double* b, int n) {
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += a[i] * b[i];
    }
    return sum;
}

// Function to compute direction cosines
double compute_direction(double alpha_deg, double beta_deg, double d[3]) {
    double rad_alpha = alpha_deg * M_PI / 180.0;
    double rad_beta  = beta_deg  * M_PI / 180.0;

    d[0] = cos(rad_alpha); // cos α
    d[1] = cos(rad_beta);  // cos β

    double sum_known = d[0]*d[0] + d[1]*d[1];
    double cos_gamma = sqrt(fmax(0.0, 1.0 - sum_known));

    d[2] = cos_gamma;  // cos γ

    return cos_gamma;
}
