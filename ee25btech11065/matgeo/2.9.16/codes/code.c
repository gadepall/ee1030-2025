#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y, z;
} Vector;

Vector cross_product(Vector v1, Vector v2);
Vector add_vectors(Vector v1, Vector v2);
int is_zero_vector(Vector v);
Vector check_collinearity_condition(Vector a, Vector b, Vector c);

int is_zero_vector(Vector v) {
    const double EPSILON = 1e-9;
    return (fabs(v.x) < EPSILON && fabs(v.y) < EPSILON && fabs(v.z) < EPSILON);
}

Vector cross_product(Vector v1, Vector v2) {
    Vector result;
    result.x = v1.y * v2.z - v1.z * v2.y;
    result.y = v1.z * v2.x - v1.x * v2.z;
    result.z = v1.x * v2.y - v1.y * v2.x;
    return result;
}

Vector add_vectors(Vector v1, Vector v2) {
    Vector result;
    result.x = v1.x + v2.x;
    result.y = v1.y + v2.y;
    result.z = v1.z + v2.z;
    return result;
}

Vector check_collinearity_condition(Vector a, Vector b, Vector c) {
    Vector a_cross_b = cross_product(a, b);
    Vector b_cross_c = cross_product(b, c);
    Vector c_cross_a = cross_product(c, a);

    Vector temp_sum = add_vectors(a_cross_b, b_cross_c);
    Vector final_sum = add_vectors(temp_sum, c_cross_a);
    
    return final_sum;
}


