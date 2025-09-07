#include <stdio.h>
#include <math.h>
#include "matfun.h"

int main() {
    double P[3] = {3.0, -2.0, 5.0};
    double distance = 5.0 * sqrt(2.0);

    double roots[2];
    solve_y_coordinate(P, distance, roots);

    if (isnan(roots[0]) || isnan(roots[1])) {
        printf("No real solutions exist for the given distance.\n");
    } else {
        printf("The points on the Y-axis at distance %.2f from P(3, -2, 5) are:\n", distance);
        printf("Q1 = (0, %.2f, 0)\n", roots[0]);
        printf("Q2 = (0, %.2f, 0)\n", roots[1]);
    }

    return 0;
}
