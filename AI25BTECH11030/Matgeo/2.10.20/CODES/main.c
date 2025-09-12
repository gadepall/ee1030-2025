#include <stdio.h>
#include "matfun.h"

void print_vector(const char* name, const double v[3]) {
    printf("%s = (%.2f, %.2f, %.2f)\n", name, v[0], v[1], v[2]);
}

int main() {
    double u[3] = {1, 2, 3};
    double v[3] = {4, 5, 6};
    double w[3] = {7, 8, 9};

    double cross_vw[3];
    cross_product(v, w, cross_vw);

    double dot_u_crossvw = dot_product(u, cross_vw);
    printf("u · (v × w) = %.2f\n", dot_u_crossvw);

    double dot_uv = dot_product(u, v);
    printf("(u · v) = %.2f\n", dot_uv);

    printf("(u · v) · w is NOT meaningful as dot product of scalar and vector.\n");

    printf("(u · v) * w (scalar multiplication) = (%.2f, %.2f, %.2f)\n",
           dot_uv * w[0], dot_uv * w[1], dot_uv * w[2]);

    printf("v · w = %.2f\n", dot_product(v, w));
    printf("u × (v · w) is NOT meaningful as cross product of vector and scalar.\n");

    return 0;
}
