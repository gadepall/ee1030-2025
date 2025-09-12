#include <stdio.h>
#include <stdbool.h>

// Function to check collinearity using the matrix method
bool check_collinearity_matrix(int h, int a, int b, int k) {
    if (h == 0 || k == 0) {
        printf(" Invalid input: h and k must be non-zero.\n");
        return false;
    }

    // Step 1: Construct the matrix from vector differences
    int row1_col1 = a - h;
    int row1_col2 = b;
    int row2_col1 = -h;
    int row2_col2 = k;

    printf("Collinearity matrix before row operations:\n");
    printf("[ %d\t%d ]\n", row1_col1, row1_col2);
    printf("[ %d\t%d ]\n", row2_col1, row2_col2);

    // Step 2: Simulate row operation R1 = R1 - R2 (for illustration)
    int new_r1_col1 = row1_col1 - row2_col1; // a
    int new_r1_col2 = row1_col2 - row2_col2; // b - k

    printf("\nAfter row operation R1 = R1 - R2:\n");
    printf("[ %d\t%d ]\n", new_r1_col1, new_r1_col2);
    printf("[ %d\t%d ]\n", row2_col1, row2_col2);

    // Step 3: Check the condition (a/h + b/k == 1) without floating point
    int lhs = a * k + b * h;
    int rhs = h * k;

    printf("\nChecking condition: (a/h + b/k == 1)\n");
    printf("Computed: (%d * %d + %d * %d) = %d\n", a, k, b, h, lhs);
    printf("Expected: (%d * %d) = %d\n", h, k, rhs);

    return (lhs == rhs);
}

int main() {
    // Example input values (change as needed)
    int h = 5;
    int a = 2;
    int b = 3;
    int k = 4;

    printf("Checking collinearity for points:\n");
    printf("A = (%d, 0), B = (%d, %d), C = (0, %d)\n\n", h, a, b, k);

    if (check_collinearity_matrix(h, a, b, k)) {
        printf("\nPoints are collinear (Matrix rank = 1 and a/h + b/k = 1).\n");
    } else {
        printf("\n Points are NOT collinear (Condition fails).\n");
    }

    return 0;
}