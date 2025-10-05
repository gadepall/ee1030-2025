
#include <stdio.h>

void get_circle_data(double *c1, double *r1, double *c2, double *r2, double *chord_y) {
    // Circle 1 center (1,3), radius 2
    c1[0] = 1; c1[1] = 3;
    *r1 = 2;

    // Circle 2 center (2,1), unknown radius
    c2[0] = 2; c2[1] = 1;
    *r2 = 2;  // radius determined by chord distance

    // chord line y=3
    *chord_y = 3;
}

