#include <math.h>
#include <stdio.h>

void vector_subtract(double* res, const double* u, const double* v) {
    for (int i = 0; i < 3; i++) {
        res[i] = u[i] - v[i];
    }
}

double dot_product(const double* u, const double* v) {
    double sum = 0.0;
    for (int i = 0; i < 3; i++) {
        sum += u[i] * v[i];
    }
    return sum;
}

void cross_product(double* res, const double* u, const double* v) {
    res[0] = u[1] * v[2] - u[2] * v[1];
    res[1] = u[2] * v[0] - u[0] * v[2];
    res[2] = u[0] * v[1] - u[1] * v[0];
}

double magnitude(const double* v) {
    double sum = 0.0;
    for (int i = 0; i < 3; i++) {
        sum += v[i] * v[i];
    }
    return sqrt(sum);
}

int is_right_angle(const double* u, const double* v) {
    double dp = dot_product(u, v);
    if (fabs(dp) < 1e-8) {
        return 1;
    }
    return 0;
}

double triangle_area(const double* u, const double* v) {
    double cross[3];
    cross_product(cross, u, v);
    return 0.5 * magnitude(cross);
}

int which_right_angle(const double* A, const double* B, const double* C) {
    double AB[3], AC[3], BA[3], BC[3], CA[3], CB[3];
    vector_subtract(AB, B, A);
    vector_subtract(AC, C, A);
    vector_subtract(BA, A, B);
    vector_subtract(BC, C, B);
    vector_subtract(CA, A, C);
    vector_subtract(CB, B, C);
    if (is_right_angle(AB, AC)) return 1;
    if (is_right_angle(BA, BC)) return 2;
    if (is_right_angle(CA, CB)) return 3;
    return 0;
}

