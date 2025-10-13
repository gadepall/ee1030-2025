#include <stdio.h>
#include <stdlib.h>

// Function to find GCD (used for boundary lattice points)
int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

// Function to find number of boundary points on one edge
int boundary_points(int x1, int y1, int x2, int y2) {
    return gcd(abs(x2 - x1), abs(y2 - y1)) + 1;
}

// Function to find total interior lattice points using Pick's theorem
int interior_points(int x1, int y1, int x2, int y2, int x3, int y3) {
    // Area = 1/2 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
    float area = 0.5 * (float)abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2));

    // Boundary points on all three sides
    int b1 = boundary_points(x1, y1, x2, y2);
    int b2 = boundary_points(x2, y2, x3, y3);
    int b3 = boundary_points(x3, y3, x1, y1);

    // Subtract 3 since each vertex is counted twice
    int B = b1 + b2 + b3 - 3;

    // Pick’s theorem: A = I + B/2 - 1  =>  I = A - B/2 + 1
    int I = (int)(area - (float)B/2 + 1);

    return I;
}
