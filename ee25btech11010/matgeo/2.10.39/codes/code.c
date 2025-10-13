#include <math.h>

typedef struct {
    double x;
    double y;
    double z;
} Vec3;

Vec3 find_unit_vector_c(void) {
    double a[3] = {2, 1, 1};
    double b[3] = {1, 2, -1};

    double dot_ab = a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
    double dot_aa = a[0]*a[0] + a[1]*a[1] + a[2]*a[2];
    double k = - (double)dot_aa / dot_ab;

    double x = a[0] + k*b[0];
    double y = a[1] + k*b[1];
    double z = a[2] + k*b[2];

    double mag = sqrt(x*x + y*y + z*z);

    Vec3 result;
    result.x = x / mag;
    result.y = y / mag;
    result.z = z / mag;

    return result;
}
