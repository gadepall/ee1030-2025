// triangle.c
#include <math.h>

float triangle_area(float ax, float ay, float bx, float by, float cx, float cy) {
    // Using determinant (matrix method)
    float area = fabs(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by)) / 2.0;
    return area;
}

