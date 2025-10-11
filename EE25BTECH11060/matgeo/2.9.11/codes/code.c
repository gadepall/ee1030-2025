#include <stdio.h>
#include <math.h>

double dot_product(double a[], double b[]) {
    return a[0]*b[0] + a[1]*b[1];
}

double norm(double v[]) {
    return sqrt(v[0]*v[0] + v[1]*v[1]);
}

void normalize(double v[]) {
    double n = norm(v);
    if (n != 0) {
        v[0] /= n;
        v[1] /= n;
    }
}

int main() {
    double a[2] = {1, 2};
    double b[2] = {2, 1};

    normalize(a);
    normalize(b);

    double cos_theta = dot_product(a, b);
    double theta = acos(cos_theta); 

    double diff[2] = {0.5 * (a[0] - b[0]), 0.5 * (a[1] - b[1])};
    double lhs = norm(diff); 

    double rhs = sin(theta / 2.0);

    printf("Angle θ (in degrees): %.6f\n", theta * (180.0 / M_PI));
    printf("||0.5(a - b)||       = %.6f\n", lhs);
    printf("sin(θ / 2)           = %.6f\n", rhs);
    printf("Difference           = %.6e\n", fabs(lhs - rhs));

    return 0;
}
