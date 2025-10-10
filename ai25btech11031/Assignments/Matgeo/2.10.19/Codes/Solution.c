#include <stdio.h>
#include "Solution.h"

int main() {
    int u[3], v[3], w[3];
    int temp[3];
    int A, B, C, D;

    // Input vectors
    printf("Enter vector u (x y z): ");
    scanf("%d %d %d", &u[0], &u[1], &u[2]);
    printf("Enter vector v (x y z): ");
    scanf("%d %d %d", &v[0], &v[1], &v[2]);
    printf("Enter vector w (x y z): ");
    scanf("%d %d %d", &w[0], &w[1], &w[2]);

    // A = u · (v × w)
    cross(v, w, temp);
    A = dot(u, temp);

    // B = v · (u × w)
    cross(u, w, temp);
    B = dot(v, temp);

    // C = (v × w) · u
    cross(v, w, temp);
    C = dot(temp, u);

    // D = (u × v) · w
    cross(u, v, temp);
    D = dot(temp, w);

    // Print results
    printf("\nResults:\n");
    printf("A = u · (v × w) = %d\n", A);
    printf("B = v · (u × w) = %d\n", B);
    printf("C = (v × w) · u = %d\n", C);
    printf("D = (u × v) · w = %d\n", D);

    // Check which is different
    if (A == C && A == D && B != A) {
        printf("\n=> Expression B is different.\n");
    } else if (B == C && B == D && A != B) {
        printf("\n=> Expression A is different.\n");
    } else if (A == B && A == D && C != A) {
        printf("\n=> Expression C is different.\n");
    } else if (A == B && A == C && D != A) {
        printf("\n=> Expression D is different.\n");
    } else {
        printf("\n=> No unique difference found (all may be equal or zero).\n");
    }

    return 0;
}

