#include <stdio.h>
#include <math.h>
#include "vector_solver.h"

int main() {
    double magnitude_c = sqrt(3);  // Change to sqrt(5) or other values to test
    VectorSolution sol = solve_vector_dependence(magnitude_c);

    if (sol.valid) {
        printf("Solution found:\n");
        printf("alpha = ±%.3f\n", sol.alpha);
        printf("beta  = %.3f\n", sol.beta);
    } else {
        printf("No valid solution for given magnitude.\n");
    }

    return 0;
}

