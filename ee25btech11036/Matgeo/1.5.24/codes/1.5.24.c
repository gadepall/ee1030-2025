#include <stdio.h>

int main() {
    // -------------------------------------------------
    // Problem statement
    // -------------------------------------------------
    printf("Problem 1.5.24:\n");
    printf("A line intersects the Y-axis and X-axis at P=(0,b) and Q=(c,0).\n");
    printf("If (2,-5) is the midpoint of PQ, find P and Q.\n\n");

    // -------------------------------------------------
    // Step (i): Rank / Collinearity relation
    // -------------------------------------------------
    printf("Step (i): Rank / Collinearity condition\n");
    printf("From collinearity, (b+5)(c-2) = -10\n\n");

    // -------------------------------------------------
    // Step (ii): Midpoint condition
    // -------------------------------------------------
    printf("Step (ii): Midpoint condition\n");
    int Mx = 2, My = -5;
    int c = 2 * Mx;   // c/2 = 2 -> c = 4
    int b = 2 * My;   // b/2 = -5 -> b = -10
    printf("Midpoint gives: c = %d, b = %d\n\n", c, b);

    // -------------------------------------------------
    // Final Answer
    // -------------------------------------------------
    int Px = 0, Py = b;
    int Qx = c, Qy = 0;
    printf("Final Answer:\n");
    printf("P = (%d, %d)\n", Px, Py);
    printf("Q = (%d, %d)\n", Qx, Qy);

    // -------------------------------------------------
    // Verification of midpoint
    // -------------------------------------------------
    int midx = (Px + Qx) / 2;
    int midy = (Py + Qy) / 2;
    printf("\nVerification:\n");
    printf("Midpoint of P and Q = (%d, %d)\n", midx, midy);

    return 0;
}
