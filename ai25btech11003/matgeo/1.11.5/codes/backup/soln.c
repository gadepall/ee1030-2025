#include <stdio.h>
#include <math.h>

#define DIM 3


void add(const double u[DIM], const double v[DIM], double out[DIM]) {
    for (int i = 0; i < DIM; ++i) out[i] = u[i] + v[i];
}

double dot(const double u[DIM], const double v[DIM]) {
    double s = 0.0;
    for (int i = 0; i < DIM; ++i) s += u[i] * v[i];
    return s;
}

double norm(const double u[DIM]) {
    return sqrt(dot(u, u));
}

void scale(const double u[DIM], double s, double out[DIM]) {
    for (int i = 0; i < DIM; ++i) out[i] = s * u[i];
}

void normalize(const double u[DIM], double out[DIM]) {
    double n = norm(u);
    if (n == 0.0) {
         
        for (int i = 0; i < DIM; ++i) out[i] = 0.0;
    } else {
        scale(u, 1.0 / n, out);
    }
}

int main(void) {
    
    const double a[DIM] = {1.0, 1.0, 1.0};
    const double b[DIM] = {2.0, 4.0, -5.0};

    
    const double lambda = 1.0;
    const double c[DIM] = {lambda, 2.0, 3.0};

    
    double s[DIM];
    add(b, c, s);            // s = (3, 6, -2)

    
    double uhat[DIM];
    normalize(s, uhat);      // uhat = (3/7, 6/7, -2/7)

    
    printf("lambda = %.0f\n", lambda);
    printf("b + c = (%.2f, %.2f, %.2f)\n", s[0], s[1], s[2]);
    printf("||b + c|| = %.2f\n", norm(s));
    printf("Unit vector along (b + c) is: (%.2f, %.2f, %.2f)\n", uhat[0], uhat[1], uhat[2]);

    
    double check = dot(a, uhat);
    printf("Verification a · u = %.2f\n", check);

    return 0;
}

