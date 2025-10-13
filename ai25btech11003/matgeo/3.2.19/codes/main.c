#include <stdio.h>
#include <math.h>

int main() {
    double b = 1.5, c = 5.0;
    double a_vals[4] = {3.6, 4.1, 3.8, 3.4};
    double cosA, alpha;
    FILE *f = fopen("main.dat", "w");
    if (!f) {
        fprintf(stderr, "Error opening main.dat\n");
        return 1;
    }

    for (int i = 0; i < 4; i++) {
        double a = a_vals[i];
        cosA = (b*b + c*c - a*a) / (2.0 * b * c);
        if (cosA >= -1.0 && cosA <= 1.0) {
            alpha = acos(cosA) * 180.0 / M_PI;
            printf("Case %d: a = %.2f cm, α = %.2f°\n", i+1, a, alpha);
            fprintf(f, "%.2f\n", alpha);
        } else {
            printf("Case %d: a = %.2f cm, no valid triangle (|cos α|>1)\n", i+1, a);
            fprintf(f, "nan\n");
        }
    }

    fclose(f);
    return 0;
}

