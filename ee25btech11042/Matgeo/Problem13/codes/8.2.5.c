#include <stdio.h>
#include <math.h>
void function(double a, double b) {
    double e = sqrt(1 - (b*b)/(a*a));
    printf("The eccentricity of ellipse (e) is: %0.2lf\n", e);
    printf("The axis of the ellipse is: x = 0\n");
    printf("The vertices of the ellipse are (0.00, %.2lf) and (0.00, - %.2lf)\n", a, a);
    printf("The foci of the ellipse are (0.00, %.2lf) and (0.00, - %.2lf)\n", a*e, a*e);
    printf("The directrices of ellipse are y = %.2lf and y = - %.2lf\n", a/e, a/e);
    printf("The length of the latus rectum of the ellipse is %.2lf\n", 2*b*b/a);
}
