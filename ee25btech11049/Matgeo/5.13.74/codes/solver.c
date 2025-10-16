#include <math.h>

#if defined(_WIN32)
    #define DLLEXPORT __declspec(dllexport)
#else
    #define DLLEXPORT
#endif

DLLEXPORT double solve_determinant_2x2(double trace_A, double trace_A3) {
    // Ensure we don't divide by zero if trace_A is 0.
    if (trace_A == 0) {
        return 0.0; // Or handle as an error, e.g., return NAN.
    }
    
    // Formula: det(A) = (tr(A)^3 - tr(A^3)) / (3 * tr(A))
    return (pow(trace_A, 3) - trace_A3) / (3.0 * trace_A);
}

