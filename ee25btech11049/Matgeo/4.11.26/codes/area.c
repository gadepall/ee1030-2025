#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define EXPORT for cross-platform shared library compatibility
#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// Define a simple structure to hold 2D point coordinates
typedef struct {
    double x;
    double y;
} Point;

/**
 * @brief Helper function to calculate the determinant of a 2x2 matrix.
 * Matrix is represented as [[a, b], [c, d]].
 */
double det2x2(double a, double b, double c, double d) {
    return a * d - b * c;
}

/**
 * @brief Solves for the bounded area analytically using matrix inversion and determinants.
 *
 * 1. Models the problem as two systems of linear equations.
 * 2. Solves for intersection points using matrix inversion.
 * 3. Calculates the area of the resulting triangle using the determinant of its vectors.
 *
 * @param p1 Pointer to a Point struct to store the first calculated intersection.
 * @param p2 Pointer to a Point struct to store the second calculated intersection.
 * @param p3 Pointer to a Point struct to store the third vertex.
 * @return The calculated area as a double.
 */
EXPORT double calculate_area_with_matrices(Point* p1, Point* p2, Point* p3) {
    // --- 1. Find Intersection for y = x - 1 and y = 1 ---
    // System in matrix form:
    // [ 1 -1 ] [x] = [1]
    // [ 0  1 ] [y]   [1]
    double det_A1 = det2x2(1.0, -1.0, 0.0, 1.0);
    if (fabs(det_A1) < 1e-9) return -1; // Avoid division by zero, matrix is singular

    // Inverse of A1 = (1/det) * [[1, 1], [0, 1]]
    p1->x = (1.0/det_A1) * (1.0 * 1.0 + 1.0 * 1.0); // (d*B1 - b*B2)
    p1->y = (1.0/det_A1) * (0.0 * 1.0 + 1.0 * 1.0); // (-c*B1 + a*B2)

    // --- 2. Find Intersection for y = -x + 1 and y = 1 ---
    // System in matrix form:
    // [ 1  1 ] [x] = [1]
    // [ 0  1 ] [y]   [1]
    double det_A2 = det2x2(1.0, 1.0, 0.0, 1.0);
    if (fabs(det_A2) < 1e-9) return -1; // Avoid division by zero

    // Inverse of A2 = (1/det) * [[1, -1], [0, 1]]
    p2->x = (1.0/det_A2) * (1.0 * 1.0 + -1.0 * 1.0);
    p2->y = (1.0/det_A2) * (0.0 * 1.0 + 1.0 * 1.0);

    // --- 3. The third vertex is the corner of y=|x-1| ---
    p3->x = 1.0;
    p3->y = 0.0;

    // --- 4. Calculate Area using Determinant of Vectors ---
    // Create two vectors originating from the third vertex (p3)
    // Vector v1 = p1 - p3
    double v1x = p1->x - p3->x;
    double v1y = p1->y - p3->y;
    // Vector v2 = p2 - p3
    double v2x = p2->x - p3->x;
    double v2y = p2->y - p3->y;

    // Area = 0.5 * |det([v1x, v1y], [v2x, v2y])|
    // Note: The determinant here is equivalent to the magnitude of the 2D cross product.
    double vector_determinant = det2x2(v1x, v2x, v1y, v2y);
    double area = 0.5 * fabs(vector_determinant);

    return area;
}


/**
 * @brief Frees the memory allocated for a 2D character matrix.
 *
 * @param matrix The matrix to free.
 * @param height The height (number of rows) of the matrix.
 */
EXPORT void free_matrix(char** matrix, int height) {
    if (matrix == NULL) {
        return;
    }
    for (int i = 0; i < height; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

/**
 * @brief Generates a 2D character matrix representing the plot of y=|x-1| and y=1.
 *
 * The function allocates memory for the matrix which must be freed later
 * using the free_matrix function.
 *
 * @param width The width of the plot matrix.
 * @param height The height of the plot matrix.
 * @return A 2D char array (char**) representing the plot. NULL on failure.
 */
EXPORT char** generate_plot_matrix(int width, int height) {
    // 1. Allocate memory for the matrix (array of pointers)
    char** matrix = (char**)malloc(height * sizeof(char*));
    if (matrix == NULL) {
        return NULL; // Allocation failed
    }

    // 2. Allocate memory for each row and initialize with spaces
    for (int i = 0; i < height; i++) {
        matrix[i] = (char*)malloc((width + 1) * sizeof(char)); // +1 for null terminator
        if (matrix[i] == NULL) {
            // If a row allocation fails, free all previously allocated memory
            free_matrix(matrix, i);
            return NULL;
        }
        for (int j = 0; j < width; j++) {
            matrix[i][j] = ' ';
        }
        matrix[i][width] = '\0'; // Null-terminate the string
    }

    // 3. Define the mathematical coordinate system boundaries
    double x_min = -1.0;
    double x_max = 3.0;
    double y_min = -0.5;
    double y_max = 1.5;

    // 4. Map mathematical coordinates to matrix cells
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            // Convert matrix indices (j, i) to math coordinates (x, y)
            double x = x_min + (double)j / (width - 1) * (x_max - x_min);
            double y = y_max - (double)i / (height - 1) * (y_max - y_min);

            // Define a small tolerance for floating point comparisons
            double tolerance_y = (y_max - y_min) / (2.0 * height);

            // Check if the point lies on one of the curves
            int on_abs_curve = fabs(y - fabs(x - 1.0)) < tolerance_y;
            int on_line_curve = fabs(y - 1.0) < tolerance_y;

            // Mark the boundary curves with '*'
            if (on_abs_curve || on_line_curve) {
                matrix[i][j] = '*';
            }
            // Fill the area bounded by the curves with '.'
            else if (y < 1.0 && y > fabs(x - 1.0)) {
                matrix[i][j] = '.';
            }
        }
    }

    return matrix;
}


