#include <stdio.h>

// Function to compute gcd
int gcd(int a, int b) {
    if (b == 0) return a > 0 ? a : -a;
    return gcd(b, a % b);
}

// Function to compute gcd of 4 numbers
int gcd4(int a, int b, int c, int d) {
    int g = gcd(a, b);
    g = gcd(g, c);
    g = gcd(g, d);
    return g;
}

int main() {
    int x1 = 2, y1 = 1, z1 = 0;
    int x2 = 3, y2 = -2, z2 = -2;
    int x3 = 3, y3 = 1, z3 = 7;

    // Direction vectors
    int v1x = x2 - x1, v1y = y2 - y1, v1z = z2 - z1;
    int v2x = x3 - x1, v2y = y3 - y1, v2z = z3 - z1;

    // Cross product → normal vector (a, b, c)
    int a = v1y * v2z - v1z * v2y;
    int b = v1z * v2x - v1x * v2z;
    int c = v1x * v2y - v1y * v2x;

    // Constant term d
    int d = -(a * x1 + b * y1 + c * z1);

    // Simplify using gcd
    int g = gcd4(a, b, c, d);
    a /= g; b /= g; c /= g; d /= g;

    // Make leading coefficient positive
    if (a < 0) {
        a = -a; b = -b; c = -c; d = -d;
    }

    printf("The equation of plane is: %dx + %dy + %dz + %d = 0\n", a, b, c, d);

    return 0;
}