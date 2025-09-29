#include <stdio.h>
#include <math.h>

void dot_product(double *a, double *b, int dim, double *result) {
    *result = 0.0;
    for (int i = 0; i < dim; ++i) {
        *result += a[i] * b[i];
    }
}

void scalar_mult(double *a, double k, int dim, double *result) {
    for (int i = 0; i < dim; ++i) {
        result[i] = k * a[i];
    }
}

void vector_sub(double *a, double *b, int dim, double *result) {
    for (int i = 0; i < dim; ++i) {
        result[i] = a[i] - b[i];
    }
}

void gram_schmidt(double *a, double *b, double *c, double *b1, double *c3) {
    int dim = 3;
    double a_dot_b, a_dot_a, a_dot_c, c_dot_b1, b1_dot_b1;
    double proj_a_on_b[3], proj_a_on_c[3], proj_b1_on_c[3];

    dot_product(a, a, dim, &a_dot_a);
    dot_product(b, a, dim, &a_dot_b);
    scalar_mult(a, a_dot_b / a_dot_a, dim, proj_a_on_b);
    vector_sub(b, proj_a_on_b, dim, b1);

    dot_product(c, a, dim, &a_dot_c);
    scalar_mult(a, a_dot_c / a_dot_a, dim, proj_a_on_c);
    double temp[3];
    vector_sub(c, proj_a_on_c, dim, temp);

    dot_product(b1, b1, dim, &b1_dot_b1);
    dot_product(c, b1, dim, &c_dot_b1);
    scalar_mult(b1, c_dot_b1 / b1_dot_b1, dim, proj_b1_on_c);

    for (int i = 0; i < dim; ++i)
        c3[i] = temp[i] - proj_b1_on_c[i];
}

__attribute__((visibility("default")))
void get_orthogonal_vectors(double *a, double *b, double *c, double *out_a, double *out_b1, double *out_c3) {
    for(int i=0; i<3; ++i) out_a[i]=a[i];
    gram_schmidt(a, b, c, out_b1, out_c3);
}

