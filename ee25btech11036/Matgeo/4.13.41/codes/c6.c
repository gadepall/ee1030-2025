// para.c
#include <math.h>

// Make the symbol visible in the shared object
__attribute__((visibility("default")))
double parallelogram_area(double x1, double y1, double x2, double y2) {
    // Cross product magnitude
    return fabs(x1 * y2 - x2 * y1);
}

