// matrix_solver.c
#include "matrix_solver.h"

// Solves for k such that:
// k + 2 = λ * 2
// -3 + 3k = λ * 3
// 5k + 1 = λ * 7
double find_k_for_infinite_solutions(void) {
    // Algebraic solution:
    // From k + 2 = 2λ => λ = (k + 2)/2
    // Substitute into -3 + 3k = 3λ
    // => -3 + 3k = 3*(k + 2)/2
    // => Multiply both sides by 2:
    // => -6 + 6k = 3k + 6
    // => 3k = 12 => k = 4

    return 4.0;
}

