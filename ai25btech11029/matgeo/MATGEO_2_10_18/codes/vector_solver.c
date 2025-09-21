#include <math.h>
#include "vector_solver.h"

VectorSolution solve_vector_dependence(double magnitude_c) {
    VectorSolution result;
    double beta = 1.0;
    double alpha_squared = magnitude_c * magnitude_c - beta * beta;

    if (alpha_squared < 0) {
        result.valid = 0;
        return result;
    }

    result.alpha = sqrt(alpha_squared);  // You can also return -sqrt(...) if needed
    result.beta = beta;
    result.valid = 1;
    return result;
}

