#include <stdio.h>

/*
    This function checks if three 2D points are collinear.
    Points are (x1, y1), (x2, y2), (x3, y3).
    Collinearity is determined by calculating the determinant of the matrix:
    | x1 y1 1 |
    | x2 y2 1 |
    | x3 y3 1 |
    The determinant is x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2).
    If the determinant is 0, the points are collinear.

    The function is marked with 'extern "C"' to prevent C++ name mangling,
    ensuring Python's ctypes can find it by its exact name.
*/
#ifdef __cplusplus
extern "C" {
#endif

    double check_collinearity(double x1, double y1, double x2, double y2, double x3, double y3) {
        // Calculate the determinant
        double determinant = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
        return determinant;
    }

#ifdef __cplusplus
}
#endif

