#include <stdio.h>
float find_collinear_m(float Ax, float Ay, float Bx, float By, float Cx, float coeff_m) {
    float numerator = (By - Ay) * (Cx - Ax) + Ay * (Bx - Ax);
    float denominator = coeff_m * (Bx - Ax);
    if (denominator == 0) {  
        return 0; 
    }
    return numerator / denominator;
}

