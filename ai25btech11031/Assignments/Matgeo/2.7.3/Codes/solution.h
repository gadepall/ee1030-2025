#ifndef VECTOR_UTILS_H
#define VECTOR_UTILS_H

// Cross product of 3D vectors
void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Dot product of 3D vectors
double dot_product(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Compute vector c = (a*k - (a×b)) / (||a||^2)
void compute_c(double a[3], double b[3], double k, double c[3]) {
    double cross[3];
    cross_product(a, b, cross);

    double norm_sq = dot_product(a, a); // |a|^2

    for (int i = 0; i < 3; i++) {
        c[i] = (a[i]*k - cross[i]) / norm_sq;
    }
}

#endif

