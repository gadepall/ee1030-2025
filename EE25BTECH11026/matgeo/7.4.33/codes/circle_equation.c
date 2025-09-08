#include <stdio.h>
#include <math.h>

void circle_equation(double a, double b, double c, double xd, double yd, double r) {
    // Normalize normal vector
    double norm = sqrt(a*a + b*b);
    double nx = a / norm;
    double ny = b / norm;

    // Two possible centers (D ± r * unit normal)
    double c1x = xd + r * nx;
    double c1y = yd + r * ny;
    double c2x = xd - r * nx;
    double c2y = yd - r * ny;

    // Check which center is on the same side as origin
    double origin_side = a*0 + b*0 + c;
    double c1_side = a*c1x + b*c1y + c;
    double c2_side = a*c2x + b*c2y + c;

    double h, k;
    if ((origin_side >= 0 && c1_side >= 0) || (origin_side <= 0 && c1_side <= 0)) {
        h = c1x; k = c1y;
    } else {
        h = c2x; k = c2y;
    }

    // f = h^2 + k^2 - r^2
    double f = h*h + k*k - r*r;

    printf("Equation of circle: (x - %.2lf)^2 + (y - %.2lf)^2 = %.2lf^2\n", h, k, r);
    
}

