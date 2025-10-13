#include <stdio.h>

// Function to generate two points on a line: P1 = h + k1*m,  P2 = h + k2*m
void find_line_points(double *h, double *m, double k1, double k2, double *P1, double *P2)
{
    for (int i = 0; i < 3; i++) {
        P1[i] = h[i] + k1 * m[i];
        P2[i] = h[i] + k2 * m[i];
    }
}
