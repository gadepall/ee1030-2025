#include <stdio.h>
void equidistant_line(double ax, double ay, double bx, double by, double *res) {
    double a = bx - ax;
    double b = by - ay;
    double normA_sq = ax*ax + ay*ay;
    double normB_sq = bx*bx + by*by;
    double c = (normB_sq - normA_sq) / 2.0;

    res[0] = a;
    res[1] = b; 
    res[2] = c;
}