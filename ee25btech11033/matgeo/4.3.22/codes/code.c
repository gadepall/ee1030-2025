
#include <stdio.h>


float find_intersection_x(float Ax, float Ay, float Bx, float By) {
    // The intersection point P has coordinates (Px, 0).
    // Let the ratio in which P divides AB be k:1.
    // From the section formula for the y-coordinate:
    // 0 = (k * By + 1 * Ay) / (k + 1)
    // which simplifies to k * By = -Ay, so k = -Ay / By.
    // This assumes By is not 0, which is true for the given points.
    float k = -Ay / By;

    // Now, we use the same ratio k to find the x-coordinate Px:
    // Px = (k * Bx + 1 * Ax) / (k + 1)
    float Px = (k * Bx + Ax) / (k + 1.0f);

    return Px;
}
