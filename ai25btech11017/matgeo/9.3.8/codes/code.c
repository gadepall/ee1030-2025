#include <stdio.h>

int main() {
    // Conic: y = x^2
    double V[2][2] = {{1, 0}, {0, 0}};
    double u[2] = {0, -0.5};
    double f = 0;

    // Line: y = x
    double n[2] = {1, -1};
    double c = 0;

    // Intersection points
    double P1[2] = {0, 0};
    double P2[2] = {1, 1};

    printf("# Parabola (conic form)\n");
    printf("V = [[%lf, %lf], [%lf, %lf]]\n", V[0][0], V[0][1], V[1][0], V[1][1]);
    printf("u = [[%lf], [%lf]]\n", u[0], u[1]);
    printf("f = %lf\n", f);

    printf("\n# Line (normal form)\n");
    printf("n = [[%lf], [%lf]]\n", n[0], n[1]);
    printf("c = %lf\n", c);

    printf("\n# Intersection Points\n");
    printf("P1 = [[%lf], [%lf]]\n", P1[0], P1[1]);
    printf("P2 = [[%lf], [%lf]]\n", P2[0], P2[1]);

    return 0;
}
