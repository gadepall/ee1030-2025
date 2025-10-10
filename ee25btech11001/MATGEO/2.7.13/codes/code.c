#include <math.h>

double triangleArea(double x1, double y1, double x2, double y2, double x3, double y3) {
    return fabs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0);
}

double findArea(double x1, double y1,
                double x2, double y2,
                double x3, double y3,
                double x4, double y4) {
    // Split into triangles: ABC and ACD
    double area1 = triangleArea(x1, y1, x2, y2, x3, y3);
    double area2 = triangleArea(x1, y1, x3, y3, x4, y4);
    return area1 + area2;
}

