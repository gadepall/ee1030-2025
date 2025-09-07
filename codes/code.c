
#include <stdio.h>

//dimension 
#define D 3

//compute C = U - V  (vector subtraction) 
void vec_sub(const int U[D], const int V[D], int C[D]) {
    for (int i = 0; i < D; ++i) C[i] = U[i] - V[i];
}

// compute dot = U^T * V  (inner product) 
int dot(const int U[D], const int V[D]) {
    int s = 0;
    for (int i = 0; i < D; ++i) s += U[i] * V[i];
    return s;
}

// multiply vector by scalar: R = k * V 
void scalar_mul(int k, const int V[D], int R[D]) {
    for (int i = 0; i < D; ++i) R[i] = k * V[i];
}

//print row-vector like [a b c] 
void print_rowvec(const int V[D]) {
    printf("[");
    for (int i = 0; i < D; ++i) {
        printf("%d", V[i]);
        if (i < D-1) printf("  ");
    }
    printf("]");
}

int main(void) {
    // Given points (column vectors) A and B 
    int A[D] = {3, 4, -5};
    int B[D] = {-2, 1, 4};

    // Step 1: compute B - A 
    int BminusA[D];
    vec_sub(B, A, BminusA);

    // Step 2: compute left-hand row vector = 2 (B - A)^T  (we store as a row) 
    int left_row[D];
    scalar_mul(2, BminusA, left_row);

    // Step 3: compute RHS scalar = B^T B - A^T A  (dot products) 
    int BB = dot(B, B);
    int AA = dot(A, A);
    int rhs = BB - AA;

    // Output (matrix-theory style) 
    printf("Using matrix theory:  2(B - A)^T X = B^T B - A^T A\n\n");

    printf("B - A (column vector) = ");
    print_rowvec(BminusA);   // prints as row for compactness 
    printf("  (i.e. column vector with these entries)\n");

    printf("Left row vector 2(B - A)^T = ");
    print_rowvec(left_row);
    printf("\n");

    printf("RHS scalar B^T B - A^T A = %d - %d = %d\n\n", BB, AA, rhs);

    // Print final plane equation in standard algebraic form 
    // left_row corresponds to coefficients [a b c] so equation is a x + b y + c z = rhs 
    printf("Hence the equation of the plane (matrix form) is:\n");
    printf("  ");
    print_rowvec(left_row);
    printf("  X = %d\n\n", rhs);

    // also print conventional algebraic equation 
    printf("Or in coordinate form:\n");
    printf("  %dx + %dy + %dz = %d\n", left_row[0], left_row[1], left_row[2], rhs);

    return 0;
}