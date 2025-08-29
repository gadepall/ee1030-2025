#include <stdio.h>

float findM(float Ax, float Ay, float Bx, float By, float Px) {
    float k = (Px - Ax) / (Bx - Px);
    float m = (k * By + Ay) / (k + 1);
    return m;
}
