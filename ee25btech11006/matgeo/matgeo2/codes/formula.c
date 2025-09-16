#include <stdio.h>
#include <math.h>

int main() {
    int Ax = 2, Ay = -4;
    int Px = 3, Py = 8;
    int Qx = -10;

     // Quadratic from ||A-P||^2 = ||A-Q||^2
     // (Ax - Px)^2 + (Ay - Py)^2 = (Ax - Qx)^2 + (Ay - y)^2
    int a = 1, b = 8, c = 15;
    int discrim = b*b - 4*a*c;

    int y1 = (-b + (int)sqrt(discrim)) / (2*a);
    int y2 = (-b - (int)sqrt(discrim)) / (2*a);

    // Distance ||P-Q|| for each y
    double d1 = sqrt((Px - Qx)*(Px - Qx) + (Py - y1)*(Py - y1));
    double d2 = sqrt((Px - Qx)*(Px - Qx) + (Py - y2)*(Py - y2));

    return 0;
}