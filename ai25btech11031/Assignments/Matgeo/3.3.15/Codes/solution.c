#include <stdio.h>
#include <math.h>
#include "solution.h"

int main() {
    double BC, AD, angleA;
    printf("Enter length BC: ");
    scanf("%lf", &BC);
    printf("Enter length of median AD: ");
    scanf("%lf", &AD);
    printf("Enter angle A (in degrees): ");
    scanf("%lf", &angleA);

    // Fix B at (0,0) and C at (BC,0)
    Point B = {0, 0};
    Point C = {BC, 0};
    Point D = {(B.x + C.x)/2, (B.y + C.y)/2};

    // Circle with center D and radius AD
    double r1 = AD;

    // Angle condition: circumcircle with radius BC/(2*sinA)
    double A_rad = angleA * M_PI / 180.0;
    double R = BC / (2.0 * sin(A_rad));

    // Two possible centers of the angle-locus circle
    Point O1 = {D.x, D.y + R};
    Point O2 = {D.x, D.y - R};

    Point p1, p2;

    printf("\nPossible coordinates of A:\n");

    // Check intersections for O1
    if (circle_intersections(D, r1, O1, R, &p1, &p2)) {
        printf("A1 = (%.3f, %.3f)\n", p1.x, p1.y);
        printf("A2 = (%.3f, %.3f)\n", p2.x, p2.y);
    }

    // Check intersections for O2
    if (circle_intersections(D, r1, O2, R, &p1, &p2)) {
        printf("A3 = (%.3f, %.3f)\n", p1.x, p1.y);
        printf("A4 = (%.3f, %.3f)\n", p2.x, p2.y);
    }

    return 0;
}

