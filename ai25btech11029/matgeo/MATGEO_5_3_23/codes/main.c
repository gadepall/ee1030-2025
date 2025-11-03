// main.c
#include <stdio.h>
#include "matrix_solver.h"

int main() {
    double k = find_k_for_infinite_solutions();
    printf("Value of k for infinite solutions: %.2f\n", k);
    return 0;
}
  
