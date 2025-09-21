#include <stdio.h>

int check_perpendicular(double x1, double y1, double x2, double y2,
                        double x3, double y3, double x4, double y4) {
    double v1x = x2 - x1;
    double v1y = y2 - y1;
    double v2x = x4 - x3;
    double v2y = y4 - y3;

    double dot = v1x * v2x + v1y * v2y;

    if (dot == 0.0) {
        return 1; 
    } else {
        return 0; 
    }
}
