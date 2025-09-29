
#include <stdio.h>

// Compute the coordinates of R dividing segment PQ in the internal ratio m:n
// Inputs: (x1,y1) = P, (x2,y2) = Q, ratio m:n
// Outputs: *rx, *ry = R
// Signature designed to be ctypes-friendly.
#ifdef _WIN32
  #define API __declspec(dllexport)
#else
  #define API
#endif

API void findPoint(double x1, double y1,
                   double x2, double y2,
                   double m,  double n,
                   double* rx, double* ry) {
    double denom = m + n;
    if (denom == 0.0) {
        // Degenerate ratio; return NaNs as a signal
        *rx = 0.0/0.0;
        *ry = 0.0/0.0;
        return;
    }
    *rx = (n * x1 + m * x2) / denom;
    *ry = (n * y1 + m * y2) / denom;
}
