#include <stdio.h>
#include <math.h>

int main() {
    double x1 = 1, y1 = -3;
    double x2 = 4, y2;  // y2 = p (unknown)
    double x3 = -9, y3 = 7;
    double area = 15.0;

    // Based on formula:
    // area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    // We solve for y2 (p):

    // Let A = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
    // 2*area = |A|
    // So, A = ± 2*area

    double two_area = 2 * area;

    // Express A in terms of y2:
    // A = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
    // = x1*y2 - x1*y3 + x2*y3 - x2*y1 + x3*y1 - x3*y2
    // Group y2 terms:
    // (x1 - x3)*y2 + (x2*y3 - x2*y1 + x3*y1 - x1*y3) = A

    double coeff_y2 = x1 - x3;  // 1 - (-9) = 10
    double constant_part = x2*y3 - x2*y1 + x3*y1 - x1*y3;

    // A = coeff_y2*y2 + constant_part
    // => y2 = (A - constant_part) / coeff_y2

    // Two cases due to absolute value:
    double A1 = two_area;
    double A2 = -two_area;

    double p1 = (A1 - constant_part) / coeff_y2;
    double p2 = (A2 - constant_part) / coeff_y2;

    printf("Possible values of p are: %.2f and %.2f\n", p1, p2);

    return 0;
}
