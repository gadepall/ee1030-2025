#include <stdio.h>
#include <math.h>

double find_distance(double x1, double y1, double x2, double y2){
    double d = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2));
    return d;
}
