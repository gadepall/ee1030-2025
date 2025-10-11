#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;

    // Open output file
    fp = fopen("answer.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // ---------------- Example 1: p + q + r = 0 ----------------
    double p1 = 1, q1 = 2, r1 = -3; // satisfies p + q + r = 0
    fprintf(fp, "Example 1:\n");
    fprintf(fp, "Given values: p = %.2lf, q = %.2lf, r = %.2lf\n", p1, q1, r1);

    if (fabs(p1 + q1 + r1) < 1e-9 || (fabs(p1 - q1) < 1e-9 && fabs(q1 - r1) < 1e-9)) {
        fprintf(fp, "→ The system has a NON-TRIVIAL solution.\n");
        if (fabs(p1 + q1 + r1) < 1e-9)
            fprintf(fp, "  Condition satisfied: p + q + r = 0\n\n");
        else
            fprintf(fp, "  Condition satisfied: p = q = r\n\n");
    } else {
        fprintf(fp, "→ The system does NOT have a non-trivial solution.\n\n");
    }

    // ---------------- Example 2: p = q = r ----------------
    double p2 = 5, q2 = 5, r2 = 5; // satisfies p = q = r
    fprintf(fp, "Example 2:\n");
    fprintf(fp, "Given values: p = %.2lf, q = %.2lf, r = %.2lf\n", p2, q2, r2);

    if (fabs(p2 + q2 + r2) < 1e-9 || (fabs(p2 - q2) < 1e-9 && fabs(q2 - r2) < 1e-9)) {
        fprintf(fp, "→ The system has a NON-TRIVIAL solution.\n");
        if (fabs(p2 + q2 + r2) < 1e-9)
            fprintf(fp, "  Condition satisfied: p + q + r = 0\n");
        else
            fprintf(fp, "  Condition satisfied: p = q = r\n");
    } else {
        fprintf(fp, "→ The system does NOT have a non-trivial solution.\n");
    }

    fclose(fp);
    printf("Results for both examples written to answer.dat\n");
    return 0;
}

