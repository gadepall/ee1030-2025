#include <stdio.h>
#include <math.h>

int main(void) {
    double abs_a = 12.0;
    double abs_b = 4.0 * sqrt(3.0);
    double bT_c = 24.0;

    double abs_b_sq = abs_b * abs_b;
    double bT_a = -(bT_c + abs_b_sq);

    double abs_a_sq = abs_a * abs_a;
    double abs_c_sq = abs_a_sq + abs_b_sq + 2.0 * bT_a;
    double abs_c = sqrt(fmax(0.0, abs_c_sq));

    double left_a = abs_c_sq / 2.0 - abs_a;
    int is_a_true = (fabs(left_a - 12.0) < 1e-9);

    double left_b = abs_c_sq / 2.0 + abs_a;
    int is_b_true = (fabs(left_b - 30.0) < 1e-9);

    int is_d_true = (fabs(bT_a + 72.0) < 1e-9);

    double cos_theta = bT_a / (abs_a * abs_b);
    if (cos_theta > 1.0) cos_theta = 1.0;
    if (cos_theta < -1.0) cos_theta = -1.0;
    double sin_theta = sqrt(fmax(0.0, 1.0 - cos_theta * cos_theta));
    double cross_mag = 2.0 * abs_a * abs_b * sin_theta;
    double target_c = 48.0 * sqrt(3.0);
    int is_c_true = (fabs(cross_mag - target_c) < 1e-9);

    printf("Given: |a| = %.10g, |b| = %.10g, b^T c = %.10g\n", abs_a, abs_b, bT_c);
    printf("Computed: a^T b = %.10g\n", bT_a);
    printf("|c|^2 = %.10g, |c| = %.10g\n", abs_c_sq, abs_c);
    printf("cos(theta) = %.10g, sin(theta) = %.10g\n", cos_theta, sin_theta);
    printf("2 * |a x b| = %.10g, target = %.10g\n\n", cross_mag, target_c);

    printf("Results (True / False):\n");
    printf("(a) (|c|^2/2 - |a| == 12): %s\n", is_a_true ? "True" : "False");
    printf("(b) (|c|^2/2 + |a| == 30): %s\n", is_b_true ? "True" : "False");
    printf("(c) (|a x b + c x a| == 48*sqrt(3)): %s\n", is_c_true ? "True" : "False");
    printf("(d) (a^T b == -72): %s\n", is_d_true ? "True" : "False");

    printf("\nSummary: True = {");
    int first = 1;
    if (is_a_true) { if (!first) printf(", "); printf("(a)"); first = 0; }
    if (is_c_true) { if (!first) printf(", "); printf("(c)"); first = 0; }
    if (is_d_true) { if (!first) printf(", "); printf("(d)"); first = 0; }
    printf("}\nFalse = {");
    if (!is_a_true) { printf("(a) "); }
    if (!is_b_true) { if (!first) printf(", "); printf("(b)"); }
    printf("}\n");

    return 0;
}
