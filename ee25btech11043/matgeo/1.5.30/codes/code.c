#include <stdio.h>

// Function to calculate the coordinates of the other end of the diameter
void formula(double x1, double y1, double xc, double yc, double *x2, double *y2) {
    *x2 = 2 * xc - x1;
    *y2 = 2 * yc - y1;
}

int main() {
    double x1 = 2;
    double y1 = 3;
    double xc = -2;
    double yc = 5;
    double x2, y2;

    formula(x1, y1, xc, yc, &x2, &y2);

   
    return 0;
}
