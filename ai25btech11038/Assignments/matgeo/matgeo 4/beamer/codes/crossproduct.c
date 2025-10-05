#include <math.h>

double triangle_area(double x1, double y1, double x2, double y2, double x3, double y3) {
    double area = fabs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0);
    return area;
}