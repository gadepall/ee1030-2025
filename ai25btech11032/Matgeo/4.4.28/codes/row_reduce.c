#include <stdio.h>

/* Compute multiplier = a21 / a11.
   If a11 == 0, print "Error" and return 0.0 .
*/
double compute_multiplier(double a11, double a21) {
    if (a11 == 0.0) {
        printf("Error\n");
        return 0.0;
    }
    return a21 / a11;
}

/* Perform row op: out2[j] = r2[j] - (r2[0]/r1[0]) * r1[j] for j=0..2
   If r1[0] == 0, print "Error" and set out2 to zeros.
*/
void apply_row_op(const double r1[3], const double r2[3], double out2[3]) {
    if (r1[0] == 0.0) {
        printf("Error\n");
        out2[0] = out2[1] = out2[2] = 0.0;
        return;
    }
    double mult = r2[0] / r1[0];
    for (int j = 0; j < 3; ++j) {
        out2[j] = r2[j] - mult * r1[j];
    }
}

