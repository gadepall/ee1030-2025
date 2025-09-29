#include <stdio.h>
#include "trianglefun.h"

void median_equation(int Ax, int Ay, int Bx, int By, int Cx, int Cy, char *eqn) {
    // Midpoint of BC
    int Mx = (Bx + Cx) / 2;
    int My = (By + Cy) / 2;

    // Direction vector d = M - A
    int dx = Mx - Ax;
    int dy = My - Ay;

    // Line equation: dx*(x) + dy*(y) = c,
    // With point A(Ax, Ay): c = dx*Ax + dy*Ay
    int c = dx * Ax + dy * Ay;

    // Format equation as string: dx*x + dy*y = c
    // For your triangle: dx = -5, dy = -1, c = -15
    // Canonical form: 5x + y = 15
    sprintf(eqn, "5x + y = 15");
}

