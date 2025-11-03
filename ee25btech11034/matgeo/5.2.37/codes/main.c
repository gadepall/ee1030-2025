#include <stdio.h>
#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// Function to solve 2x2 linear equations using Cramer's rule
// a1*x + b1*y = c1
// a2*x + b2*y = c2
void solve_intersection(double a1, double b1, double c1,
                        double a2, double b2, double c2,
                        double *x, double *y) {
    double det = a1*b2 - a2*b1;
    if(det == 0) {
        *x = *y = 0; // No unique solution
        return;
    }
    *x = (c1*b2 - c2*b1) / det;
    *y = (a1*c2 - a2*c1) / det;
}
