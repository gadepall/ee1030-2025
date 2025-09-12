#include <stdio.h>

// Function to fill coordinates of P and Q
void get_points(int *Px, int *Py, int *Qx, int *Qy) {
    int mx = 2, my = 5;   // midpoint given

    *Px = 0;
    *Py = 2 * my;   // y1 = 10
    *Qx = 2 * mx;   // x1 = 4
    *Qy = 0;
}
