#include <stdio.h>

void solveSystem(double a, double lambda, double mu, double sol[2]) {
    double D = -2 * (a + 3);

    if (D != 0) {
        // Unique solution
        sol[0] = (-2 * lambda - 2 * mu) / D;  // x
        sol[1] = (3 * lambda - a * mu) / D;   // y
        printf("Unique solution exists:\n");
        printf("x = %.3f, y = %.3f\n", sol[0], sol[1]);
    } else {
        // When a = -3
        if (lambda + mu == 0)
            printf("Infinitely many solutions (system consistent)\n");
        else
            printf("No solution (system inconsistent)\n");
    }
}
