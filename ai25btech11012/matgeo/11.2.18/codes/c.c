#include <stdio.h>
#include <math.h>

// Structure to represent a 2D vector or point
typedef struct {
    float x, y;
} Vector;

// Function to subtract two vectors: result = B - A
Vector subtract(Vector A, Vector B) {
    Vector R;
    R.x = B.x - A.x;
    R.y = B.y - A.y;
    return R;
}

// Function to calculate magnitude of a vector
float magnitude(Vector A) {
    return sqrt(A.x * A.x + A.y * A.y);
}

// Function to check if two vectors are parallel (cross product = 0)
int isParallel(Vector A, Vector B) {
    float cross = A.x * B.y - A.y * B.x;
    if (fabs(cross) < 1e-6)
        return 1; // parallel
    else
        return 0; // not parallel
}

int main() {
    Vector A, B, C, M, N;
    Vector MN, BC;
    
    // Input triangle vertices
    printf("Enter coordinates of A (x y): ");
    scanf("%f %f", &A.x, &A.y);
    printf("Enter coordinates of B (x y): ");
    scanf("%f %f", &B.x, &B.y);
    printf("Enter coordinates of C (x y): ");
    scanf("%f %f", &C.x, &C.y);

    // Midpoints of AB and AC
    M.x = (A.x + B.x) / 2.0;
    M.y = (A.y + B.y) / 2.0;
    N.x = (A.x + C.x) / 2.0;
    N.y = (A.y + C.y) / 2.0;

    // Vectors MN and BC
    MN = subtract(M, N);
    BC = subtract(B, C);

    // Magnitudes
    float lenMN = magnitude(MN);
    float lenBC = magnitude(BC);

    printf("\nVector MN = (%.2f, %.2f)", MN.x, MN.y);
    printf("\nVector BC = (%.2f, %.2f)", BC.x, BC.y);

    // Check parallelism
    if (isParallel(MN, BC))
        printf("\nMN is parallel to BC.");
    else
        printf("\nMN is not parallel to BC.");

    // Check if MN is half of BC
    float ratio = lenMN / lenBC;
    printf("\nLength of MN = %.2f", lenMN);
    printf("\nLength of BC = %.2f", lenBC);
    printf("\nRatio MN/BC = %.2f", ratio);
    

FILE *file;
	file = fopen("values.dat", "w");

    if (fabs(ratio - 0.5) < 1e-6)
        fprintf(file,"\nHence, MN is half of BC.\n");
    else
        fprintf(file,"\nMN is not half of BC.\n");
   fclose(file);
   	printf("Results have been written to values.dat\n");
    return 0;
}

