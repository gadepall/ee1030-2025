#include <stdio.h>

/**
 * @brief Calculates the vertices of a triangle formed by two lines and the x-axis.
 * * @param A1, B1, C1 Coefficients of the first line (A1x + B1y + C1 = 0)
 * @param A2, B2, C2 Coefficients of the second line (A2x + B2y + C2 = 0)
 * @param ax Pointer to store the x-coordinate of vertex A
 * @param ay Pointer to store the y-coordinate of vertex A
 * @param bx Pointer to store the x-coordinate of vertex B
 * @param by Pointer to store the y-coordinate of vertex B
 * @param cx Pointer to store the x-coordinate of vertex C
 * @param cy Pointer to store the y-coordinate of vertex C
 * @return int 0 on success, -1 if lines are parallel.
 */
int findTriangleVertices(double A1, double B1, double C1, 
                         double A2, double B2, double C2, 
                         double *ax, double *ay, 
                         double *bx, double *by, 
                         double *cx, double *cy) {

    // Vertex A: Intersection of Line 1 with the x-axis (y=0)
    // A1*x + C1 = 0 => x = -C1 / A1
    *ax = -C1 / A1;
    *ay = 0.0;

    // Vertex B: Intersection of Line 2 with the x-axis (y=0)
    // A2*x + C2 = 0 => x = -C2 / A2
    *bx = -C2 / A2;
    *by = 0.0;

    // Vertex C: Intersection of Line 1 and Line 2
    // Using Cramer's rule to solve the system of equations
    double determinant = A1 * B2 - A2 * B1;

    // If the determinant is 0, the lines are parallel.
    if (determinant == 0) {
        return -1; // Indicate failure
    }

    *cx = (B1 * C2 - B2 * C1) / determinant;
    *cy = (C1 * A2 - C2 * A1) / determinant;

    return 0; // Indicate success
}


