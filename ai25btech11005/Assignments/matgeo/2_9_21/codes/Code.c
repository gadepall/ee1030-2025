#include <stdio.h>

// Function to compute cross product
void crossProduct(int a[3], int b[3], int c[3], int K) {
    c[0] = K * (a[1]*b[2] - a[2]*b[1]);  // i component
    c[1] = K * (a[2]*b[0] - a[0]*b[2]);  // j component
    c[2] = K * (a[0]*b[1] - a[1]*b[0]);  // k component
}

int main() {
    int a[3], b[3], c[3], K;

    // Input vectors a and b
    printf("Enter vector a (ax ay az): ");
    scanf("%d %d %d", &a[0], &a[1], &a[2]);

    printf("Enter vector b (bx by bz): ");
    scanf("%d %d %d", &b[0], &b[1], &b[2]);

    printf("Enter scalar K: ");
    scanf("%d", &K);

    // Compute c = K(a × b)
    crossProduct(a, b, c, K);

    // Print result
    printf("Vector c = %di + %dj + %dk\n", c[0], c[1], c[2]);

    return 0;
}