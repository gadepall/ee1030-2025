#include <stdio.h>

/*
   A rectangle PQRS has its side PQ parallel to the line y = mx
   and vertices P, Q, S on lines y=a, x=b, x=-b respectively.
   Find the locus of vertex R.
   Result: y = m*x - (a*(1+m^2))/m,  with x = ±b
*/

double find_locus(double m, double a, double x) {
    return m * x - (a * (1 + m * m)) / m;
}

int main() {
    double m, a, b;

    printf("Enter slope m: ");
    scanf("%lf", &m);

    printf("Enter constant a (line y=a): ");
    scanf("%lf", &a);

    printf("Enter constant b (lines x=±b): ");
    scanf("%lf", &b);

    // For x = +b
    double y1 = find_locus(m, a, b);
    printf("For x = %.2f, R = (%.2f, %.2f)\n", b, b, y1);

    // For x = -b
    double y2 = find_locus(m, a, -b);
    printf("For x = %.2f, R = (%.2f, %.2f)\n", -b, -b, y2);

    return 0;
}

