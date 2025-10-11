#include <stdio.h>

// Reflect a vector (dx,dy) about the X-axis
void reflect_ray(float dx, float dy, float *rx, float *ry) {
    *rx = dx;      // x component unchanged
    *ry = -dy;     // y component flipped
}
