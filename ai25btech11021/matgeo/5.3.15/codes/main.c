#include <stdio.h>
#include <stdbool.h>

bool areEqual(double a, double b, double epsilon) {
    return (a - b < epsilon) && (b - a < epsilon);
}

int main() {
    double a1 = 1, b1 = -2, c1 = -3;
    double a2 = 2, b2 = -4, c2 = 5;

    double ratio_a = a1 / a2;
    double ratio_b = b1 / b2;
    double ratio_c = c1 / c2;

    double epsilon = 1e-6;

    if (areEqual(ratio_a, ratio_b, epsilon) && !areEqual(ratio_b, ratio_c, epsilon)) {
        printf("The lines are parallel and distinct.\n");
    } else if (areEqual(ratio_a, ratio_b, epsilon) && areEqual(ratio_b, ratio_c, epsilon)) {
        printf("The lines are coincident.\n");
    } else {
        printf("The lines intersect (are not parallel).\n");
    }

    return 0;
}
