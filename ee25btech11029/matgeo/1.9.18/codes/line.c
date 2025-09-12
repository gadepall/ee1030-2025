#include <math.h>

// Function to calculate distance between two points (x1,y1) and (x2,y2)
double distance(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
}
