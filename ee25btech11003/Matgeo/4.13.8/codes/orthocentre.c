#include <stdio.h>

/**
 * @brief Calculates the orthocentre of a triangle formed by three lines in a single function.
 * * This function consolidates all steps:
 * 1. Finds two vertices of the triangle.
 * 2. Determines the equations of the two corresponding altitudes.
 * 3. Calculates the intersection of the altitudes to find the orthocentre.
 * * @param a1, b1, c1 Coefficients of the first line (a1*x + b1*y = c1).
 * @param a2, b2, c2 Coefficients of the second line.
 * @param a3, b3, c3 Coefficients of the third line.
 * @param orthocentre_x Pointer to a double to store the final x-coordinate.
 * @param orthocentre_y Pointer to a double to store the final y-coordinate.
 */
void calculateOrthocentre(double a1, double b1, double c1, 
                          double a2, double b2, double c2, 
                          double a3, double b3, double c3,
                          double* orthocentre_x, double* orthocentre_y) {
    
    // Internal variables for storing intermediate results
    double vertexA_x, vertexA_y;
    double vertexB_x, vertexB_y;
    double altA_a, altA_b, altA_c;
    double altB_a, altB_b, altB_c;
    double determinant;

    // --- Step 1: Find two vertices of the triangle ---

    // Find Vertex A (Intersection of Line 1 and Line 2)
    determinant = a1 * b2 - a2 * b1;
    if (determinant == 0) {
        printf("Error: Line 1 and Line 2 are parallel. Cannot form a triangle.\n");
        *orthocentre_x = 0;
        *orthocentre_y = 0;
        return;
    }
    vertexA_x = (b2 * c1 - b1 * c2) / determinant;
    vertexA_y = (a1 * c2 - a2 * c1) / determinant;

    // Find Vertex B (Intersection of Line 2 and Line 3)
    determinant = a2 * b3 - a3 * b2;
    if (determinant == 0) {
        printf("Error: Line 2 and Line 3 are parallel. Cannot form a triangle.\n");
        *orthocentre_x = 0;
        *orthocentre_y = 0;
        return;
    }
    vertexB_x = (b3 * c2 - b2 * c3) / determinant;
    vertexB_y = (a2 * c3 - a3 * c2) / determinant;

    // --- Step 2: Find the equations of two corresponding altitudes ---

    // Find Altitude A (passes through Vertex A, perpendicular to Line 3)
    altA_a = b3;
    altA_b = -a3;
    altA_c = altA_a * vertexA_x + altA_b * vertexA_y;

    // Find Altitude B (passes through Vertex B, perpendicular to Line 1)
    altB_a = b1;
    altB_b = -a1;
    altB_c = altB_a * vertexB_x + altB_b * vertexB_y;

    // --- Step 3: The orthocentre is the intersection of the two altitudes ---
    
    determinant = altA_a * altB_b - altB_a * altA_b;
    if (determinant == 0) {
        // This case should not happen for a valid triangle
        printf("Error: Altitudes are parallel.\n"); 
        *orthocentre_x = 0;
        *orthocentre_y = 0;
        return;
    }
    *orthocentre_x = (altB_b * altA_c - altA_b * altB_c) / determinant;
    *orthocentre_y = (altA_a * altB_c - altB_a * altA_c) / determinant;
}
