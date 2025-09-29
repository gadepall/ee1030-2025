#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to compute distance between (x1,y1) and (x2,y2)
double find_distance(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    return sqrt(dx*dx + dy*dy);
}

int main() {
    double x1 = 0, y1 = 2*sqrt(5);
    double x2 = -2*sqrt(5), y2 = 0;

    double d = find_distance(x1, y1, x2, y2);
    printf("Distance = %.4f\n", d);

    return 0;
}
