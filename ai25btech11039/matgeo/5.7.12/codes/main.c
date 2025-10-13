

#include <stdio.h>
#include <stdbool.h>

typedef struct { int a11, a12, a21, a22; } M2;

/* helpers */
M2 sub_scalar_I(M2 A, int s) {
    M2 B = A;
    B.a11 -= s;
    B.a22 -= s;
    return B;
}

M2 mul(M2 X, M2 Y) {
    M2 Z;
    Z.a11 = X.a11*Y.a11 + X.a12*Y.a21;
    Z.a12 = X.a11*Y.a12 + X.a12*Y.a22;
    Z.a21 = X.a21*Y.a11 + X.a22*Y.a21;
    Z.a22 = X.a21*Y.a12 + X.a22*Y.a22;
    return Z;
}

bool is_zero(M2 Z) {
    return Z.a11==0 && Z.a12==0 && Z.a21==0 && Z.a22==0;
}

void printM(const char* name, M2 A) {
    printf("%s = [[%d, %d], [%d, %d]]\n", name, A.a11, A.a12, A.a21, A.a22);
}

int main(void) {
    M2 A = {4, 2, -1, 1};

    M2 Aminus2I = sub_scalar_I(A, 2);  // A - 2I
    M2 Aminus3I = sub_scalar_I(A, 3);  // A - 3I
    M2 P = mul(Aminus2I, Aminus3I);    // (A - 2I)(A - 3I)

    printM("A", A);
    printM("A - 2I", Aminus2I);
    printM("A - 3I", Aminus3I);
    printM("(A - 2I)(A - 3I)", P);

    if (is_zero(P)) {
        printf("Verified: (A - 2I)(A - 3I) = 0 (zero matrix).\n");
    } else {
        printf("Not zero — check computations.\n");
    }
    return 0;
}
