#include <stdio.h>

void echelonForm(double matrix[2][2]) {
    // Assuming matrix is 2x2
    double factor;

    // Make the first element of second row zero by row operation
    if (matrix[0][0] == 0) {
        printf("Cannot perform elimination as pivot is zero.\n");
        return;
    }
    
    factor = matrix[1][0] / matrix[0][0];

    // Subtract factor * first row from second row
    matrix[1][0] = matrix[1][0] - factor * matrix[0][0];
    matrix[1][1] = matrix[1][1] - factor * matrix[0][1];
}

int main() {
    double p;
    printf("Enter value for p: ");
    scanf("%lf", &p);

    // Create matrix with rows [p-2, -2] and [-3, 2]
    double matrix[2][2] = {
        {p - 2, -2},
        {-3, 2}
    };

    printf("Original matrix:\n");
    for(int i=0; i<2; i++) {
        for(int j=0; j<2; j++) {
            printf("%8.3f ", matrix[i][j]);
        }
        printf("\n");
    }

    echelonForm(matrix);

    printf("\nMatrix after echelon form operation:\n");
    for(int i=0; i<2; i++) {
        for(int j=0; j<2; j++) {
            printf("%8.3f ", matrix[i][j]);
        }
        printf("\n");
    }

    if (matrix[1][1] == 0) {
        printf("\nRows are linearly dependent; points are collinear for p = %.3f\n", p);
    } else {
        printf("\nRows are not linearly dependent; points are NOT collinear for p = %.3f\n", p);
    }

    return 0;
}
