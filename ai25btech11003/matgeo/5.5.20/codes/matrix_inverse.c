#include <stdio.h>
#include <stdlib.h>

void print_matrix(double matrix[3][6], int rows, int cols, const char* title) {
    printf("%s\n", title);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%10.6f ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void save_matrix_to_file(double matrix[3][6], const char* filename) {
    FILE *file = fopen(filename, "wb");
    if (file == NULL) {
        printf("Error opening file for writing\n");
        return;
    }

    // Write the inverse matrix (last 3 columns) to binary file
    for (int i = 0; i < 3; i++) {
        for (int j = 3; j < 6; j++) {
            fwrite(&matrix[i][j], sizeof(double), 1, file);
        }
    }
    fclose(file);
}

int main() {
    // Original matrix A = [[3, 0, -1], [2, 3, 0], [0, 4, 1]]
    // Augmented matrix [A | I]
    double aug_matrix[3][6] = {
        {3.0, 0.0, -1.0, 1.0, 0.0, 0.0},
        {2.0, 3.0,  0.0, 0.0, 1.0, 0.0},
        {0.0, 4.0,  1.0, 0.0, 0.0, 1.0}
    };

    print_matrix(aug_matrix, 3, 6, "Original Augmented Matrix [A | I]:");

    // Gauss-Jordan elimination to convert to RREF

    // Step 1: Make aug_matrix[0][0] = 1 by dividing R1 by 3
    double pivot = aug_matrix[0][0];
    for (int j = 0; j < 6; j++) {
        aug_matrix[0][j] /= pivot;
    }
    print_matrix(aug_matrix, 3, 6, "Step 1: R1 -> R1/3");

    // Step 2: Eliminate column 0 in rows 1 and 2
    // R2 -> R2 - 2*R1
    for (int j = 0; j < 6; j++) {
        aug_matrix[1][j] -= 2.0 * aug_matrix[0][j];
    }
    print_matrix(aug_matrix, 3, 6, "Step 2: R2 -> R2 - 2*R1");

    // Step 3: Make aug_matrix[1][1] = 1
    pivot = aug_matrix[1][1];
    for (int j = 0; j < 6; j++) {
        aug_matrix[1][j] /= pivot;
    }
    print_matrix(aug_matrix, 3, 6, "Step 3: R2 -> R2/3");

    // Step 4: Eliminate aug_matrix[2][1] 
    // R3 -> R3 - 4*R2
    for (int j = 0; j < 6; j++) {
        aug_matrix[2][j] -= 4.0 * aug_matrix[1][j];
    }
    print_matrix(aug_matrix, 3, 6, "Step 4: R3 -> R3 - 4*R2");

    // Step 5: Make aug_matrix[2][2] = 1
    pivot = aug_matrix[2][2];
    for (int j = 0; j < 6; j++) {
        aug_matrix[2][j] /= pivot;
    }
    print_matrix(aug_matrix, 3, 6, "Step 5: R3 -> R3 * 9");

    // Step 6: Eliminate aug_matrix[0][2] and aug_matrix[1][2]
    // R1 -> R1 - aug_matrix[0][2]*R3
    double factor = aug_matrix[0][2];
    for (int j = 0; j < 6; j++) {
        aug_matrix[0][j] -= factor * aug_matrix[2][j];
    }
    print_matrix(aug_matrix, 3, 6, "Step 6: R1 -> R1 + (1/3)*R3");

    // R2 -> R2 - aug_matrix[1][2]*R3  
    factor = aug_matrix[1][2];
    for (int j = 0; j < 6; j++) {
        aug_matrix[1][j] -= factor * aug_matrix[2][j];
    }
    print_matrix(aug_matrix, 3, 6, "Step 7: R2 -> R2 - (2/9)*R3");

    printf("Final Inverse Matrix A^(-1):\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 3; j < 6; j++) {
            printf("%10.6f ", aug_matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    // Save results to files
    save_matrix_to_file(aug_matrix, "main.dat");

    // Create a shared object marker file
    FILE *so_file = fopen("main.so", "w");
    if (so_file != NULL) {
        fprintf(so_file, "Matrix inverse computation completed successfully\n");
        fclose(so_file);
    }

    printf("Files main.so and main.dat have been created.\n");

    return 0;
}