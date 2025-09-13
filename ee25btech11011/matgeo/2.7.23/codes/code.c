#include <stdio.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

// Function to compute the positive value of k
EXPORT double solve_k_positive() {
    double k1 = (104.0 - 14.0) / 12.0;   // 7.5
    double k2 = (-104.0 - 14.0) / 12.0;  // -9.8333

    return (k1 > 0) ? k1 : k2;
}

int main() {
    double k = solve_k_positive();
    printf("Positive value of k: %.2lf\n", k);
    return 0;
}
