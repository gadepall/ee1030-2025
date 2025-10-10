#include <stdio.h>

int main() {
    // Line: x - (y/5) = 20
    // Normal vector n = (1, -1/5)
    double n[2] = {1.0, -0.2}; // -1/5 = -0.2

    // Direction vector m is perpendicular to n
    double m[2] = {1.0, 5.0};

    printf("Equation of line: x - y/5 - 10 = 10\n");
    printf("Normal vector (n): (%.2f, %.2f)\n", n[0], n[1]);
    printf("Direction vector (m): (%.2f, %.2f)\n", m[0], m[1]);

    return 0;
}
