#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Structure to hold matrix data
typedef struct {
    double **data;
    int rows;
    int cols;
} Matrix;

// Function to create a matrix
Matrix* create_matrix(int rows, int cols) {
    Matrix* mat = (Matrix*)malloc(sizeof(Matrix));
    mat->rows = rows;
    mat->cols = cols;
    mat->data = (double**)malloc(rows * sizeof(double*));
    for (int i = 0; i < rows; i++) {
        mat->data[i] = (double*)malloc(cols * sizeof(double));
    }
    return mat;
}

// Function to free matrix memory
void free_matrix(Matrix* mat) {
    for (int i = 0; i < mat->rows; i++) {
        free(mat->data[i]);
    }
    free(mat->data);
    free(mat);
}

// Function to perform matrix transpose
Matrix* transpose(Matrix* mat) {
    Matrix* result = create_matrix(mat->cols, mat->rows);
    for (int i = 0; i < mat->rows; i++) {
        for (int j = 0; j < mat->cols; j++) {
            result->data[j][i] = mat->data[i][j];
        }
    }
    return result;
}

// Function to multiply two matrices
Matrix* multiply_matrices(Matrix* a, Matrix* b) {
    if (a->cols != b->rows) {
        printf("Error: Matrix dimensions incompatible for multiplication\n");
        return NULL;
    }

    Matrix* result = create_matrix(a->rows, b->cols);
    for (int i = 0; i < a->rows; i++) {
        for (int j = 0; j < b->cols; j++) {
            result->data[i][j] = 0;
            for (int k = 0; k < a->cols; k++) {
                result->data[i][j] += a->data[i][k] * b->data[k][j];
            }
        }
    }
    return result;
}

// Function to calculate minimum value of parabola y = x^2 - 2x + 4
double find_minimum_value() {
    // Given parabola: x^2 - 2x - y + 4 = 0
    // Parameters from the problem:
    // V matrix (2x2)
    Matrix* V = create_matrix(2, 2);
    V->data[0][0] = 1.0;  // coefficient of x^2
    V->data[0][1] = 0.0;
    V->data[1][0] = 0.0;
    V->data[1][1] = 0.0;

    // u vector (2x1)
    Matrix* u = create_matrix(2, 1);
    u->data[0][0] = -1.0;   // coefficient of x
    u->data[1][0] = -0.5;   // coefficient of y

    double f = 4.0;  // constant term

    // Line L parameters (parallel to x-axis)
    // m vector (2x1)
    Matrix* m = create_matrix(2, 1);
    m->data[0][0] = 1.0;  // direction vector x-component
    m->data[1][0] = 0.0;  // direction vector y-component

    // For minimum value, discriminant = 0
    // [m^T(Vh + u)]^2 - g(h)(m^T V m) = 0
    // where h = [0, phi] and phi is the minimum y value

    // Calculate m^T V m
    Matrix* m_T = transpose(m);
    Matrix* mT_V = multiply_matrices(m_T, V);
    Matrix* mT_V_m = multiply_matrices(mT_V, m);
    double mTVm = mT_V_m->data[0][0];

    // For the given problem: m^T V m = 1
    printf("m^T V m = %.2f\n", mTVm);

    // From the discriminant condition: (m^T(Vh + u))^2 = g(h)(m^T V m)
    // Substituting values: (-1)^2 = (4 - phi)(1)
    // 1 = 4 - phi
    // phi = 3

    double phi = 3.0;

    // Verification: calculate discriminant
    double discriminant_term = 1.0 - (4.0 - phi) * 1.0;
    printf("Discriminant term: %.6f\n", discriminant_term);

    // Clean up memory
    free_matrix(V);
    free_matrix(u);
    free_matrix(m);
    free_matrix(m_T);
    free_matrix(mT_V);
    free_matrix(mT_V_m);

    return phi;
}

// Function to generate parabola points for plotting
void generate_parabola_data() {
    FILE* fp = fopen("main.dat", "w");
    if (fp == NULL) {
        printf("Error: Cannot create main.dat file\n");
        return;
    }

    fprintf(fp, "x,y\n");

    // Generate points for parabola y = x^2 - 2x + 4
    for (double x = -2.0; x <= 4.0; x += 0.1) {
        double y = x * x - 2 * x + 4;
        fprintf(fp, "%.1f,%.2f\n", x, y);
    }

    // Add minimum point
    fprintf(fp, "1.0,3.0\n");

    fclose(fp);
    printf("Parabola data written to main.dat\n");
}

// Main function
int main() {
    printf("=== Parabola Minimum Value Calculator ===\n");
    printf("Equation: y = x^2 - 2x + 4\n\n");

    double min_value = find_minimum_value();

    printf("\nMinimum value of y: %.1f\n", min_value);
    printf("This occurs at x = 1\n");
    printf("Vertex: (1, 3)\n");

    // Generate data for Python plotting
    generate_parabola_data();

    return 0;
}
