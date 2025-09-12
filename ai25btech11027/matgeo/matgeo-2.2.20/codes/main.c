#include <math.h>

// angle_between: takes two arrays (each 3 elements) and returns angle in degrees
double angle_between(double a[3], double b[3]) {
    double dot = 0, na = 0, nb = 0;
    double pi=3.14;
    for (int i = 0; i < 3; i++) {
        dot += a[i] * b[i];
        na += a[i] * a[i];
        nb += b[i] * b[i];
    }
    double cosv = dot / (sqrt(na) * sqrt(nb));
    if (cosv > 1.0) cosv = 1.0;
    if (cosv < -1.0) cosv = -1.0;
    return acos(cosv) * 180.0 / pi;
}
