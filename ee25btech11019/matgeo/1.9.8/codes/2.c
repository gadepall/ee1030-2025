#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to compute distance between (0,0) and (a-b,a+b)
double find_distance(double a, double b) {
    double x = a - b;
    double y = a + b;
    return sqrt(x*x + y*y);
}