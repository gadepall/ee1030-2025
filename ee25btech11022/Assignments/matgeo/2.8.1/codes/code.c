#include <stdio.h>
#include <math.h>

void find_third_vertex(double *x, double *y) {
    // Given two vertices
    double Ax = -4, Ay = 3;
    double Bx = 4,  By = 3;

    // Side length AB
    double AB = sqrt((Bx - Ax)*(Bx - Ax) + (By - Ay)*(By - Ay));

    // Midpoint M
    double Mx = (Ax + Bx) / 2.0;
    double My = (Ay + By) / 2.0;

    // Height for equilateral triangle
    double h = (sqrt(3) / 2.0) * AB;

    // Two possible third vertices (perpendicular from midpoint)
    double C1x = Mx;
    double C1y = My + h;

    double C2x = Mx;
    double C2y = My - h;

    // Choose the third vertex such that origin lies inside triangle
    // Since origin is inside, pick vertex with y < 0
    if (C1y < 0) {
        *x = C1x;
        *y = C1y;
    } else {
        *x = C2x;
        *y = C2y;
    }
}

