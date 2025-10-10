#include <stdio.h>
#include "matfun.h"

int main() {
    double P[3] = {2.0, -3.0, 4.0};
    double Q[3];

    foot_of_perpendicular_to_Y_axis(P, Q);

    printf("Foot of the perpendicular from P(2, -3, 4) to Y-axis is: (%.2f, %.2f, %.2f)\n", Q[0], Q[1], Q[2]);
    return 0;
}
