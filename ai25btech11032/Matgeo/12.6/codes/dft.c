#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Simple DFT function
// Input: real x[n], length N
// Output: real and imag parts of X[k]
void dft(const double* x, int N, double* Xr, double* Xi) {
    for (int k = 0; k < N; k++) {
        double sum_r = 0.0, sum_i = 0.0;
        for (int n = 0; n < N; n++) {
            double angle = -2.0 * M_PI * k * n / N;
            sum_r += x[n] * cos(angle);
            sum_i += x[n] * sin(angle);
        }
        Xr[k] = sum_r;
        Xi[k] = sum_i;
    }
}

