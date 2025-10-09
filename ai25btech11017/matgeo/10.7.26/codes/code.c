#include <stdio.h>
#include <math.h>

int main() {
    double m;
    double tolerance = 0.001;
    double sqrt2 = sqrt(2);
    int first = 1;

    printf("slopes = [");

    for (m = -10.0; m <= 10.0; m += 0.001) {
        double lhs = (2 * m) / sqrt(m * m + 1);

        if (fabs(fabs(lhs) - sqrt2) < tolerance) {
            if (!first) {
                printf(",");
            }
            printf("%.6g", m);
            first = 0;
        }
    }

    printf("]\n");
    return 0;
}
