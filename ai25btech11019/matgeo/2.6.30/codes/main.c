#include <stdio.h>
#include <math.h>

int main(void) {
    /* Given vertices */
    double Ax = 2.0, Ay = 6.0;
    double Bx = 5.0, By = -4.0;
    /* C = (k, 4.0) where k is unknown */

    /* Compute vector B-A */
    double v1x = Bx - Ax;   // 3
    double v1y = By - Ay;   // -10

    /* Vector C-A = (k-2, -2) symbolic; cross = v1x*( -2 ) - v1y*(k-2) */
    /* cross = 3 * (-2) - (-10) * (k - 2) = -6 + 10*(k - 2) = 10k - 26 */

    printf("Vector B - A = (%.1f, %.1f)\n", v1x, v1y);
    printf("Vector C - A = (k - 2, -2)\n\n");

    printf("Cross product (B-A) x (C-A) = 10*k - 26\n");
    printf("Area = 1/2 * |cross|\n");
    printf("Given area = 35, so |10*k - 26| = 70\n\n");

    /* Solve the two linear equations */
    double k_case1 = (70.0 + 26.0) / 10.0;   // 10k - 26 = 70  -> k = 96/10
    double k_case2 = (-70.0 + 26.0) / 10.0;  // 10k - 26 = -70 -> k = -44/10

    printf("Case 1: 10k - 26 = 70  =>  k = (70 + 26)/10 = %.5g  (== 48/5 = 9.6)\n", k_case1);
    printf("Case 2: 10k - 26 = -70 =>  k = (-70 + 26)/10 = %.5g  (== -22/5 = -4.4)\n\n", k_case2);

    /* Verify both values by computing area from cross */
    double cross1 = 10.0 * k_case1 - 26.0;
    double area1 = 0.5 * fabs(cross1);

    double cross2 = 10.0 * k_case2 - 26.0;
    double area2 = 0.5 * fabs(cross2);

    printf("Verification:\n");
    printf(" For k = %.5g : cross = %.5g, area = 0.5 * |cross| = %.5g\n", k_case1, cross1, area1);
    printf(" For k = %.5g : cross = %.5g, area = 0.5 * |cross| = %.5g\n", k_case2, cross2, area2);

    if (fabs(area1 - 35.0) < 1e-9 && fabs(area2 - 35.0) < 1e-9) {
        printf("\nBoth k values verified: area = 35 for both.\n");
    } else {
        printf("\nVerification done (if any area differs from 35, check calculations).\n");
    }

    printf("\nFinal answers: k = 48/5 (9.6) or k = -22/5 (-4.4)\n");

    return 0;
}
