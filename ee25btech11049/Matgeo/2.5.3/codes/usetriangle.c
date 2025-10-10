/**
 * @file triangle_checker.c
 * @brief A simple C library to check if three points form a right-angled triangle.
 *
 * This code is intended to be compiled into a shared library (.so on Linux/macOS,
 * .dll on Windows) and used by other programs, such as the provided Python script.
 */

/**
 * @brief Calculates the square of the Euclidean distance between two 2D points.
 *
 * Using the square of the distance avoids the need for a square root calculation,
 * which is computationally more expensive and can introduce floating-point inaccuracies.
 * The Pythagorean theorem works perfectly with squared distances.
 *
 * @param x1 The x-coordinate of the first point.
 * @param y1 The y-coordinate of the first point.
 * @param x2 The x-coordinate of the second point.
 * @param y2 The y-coordinate of the second point.
 * @return The square of the distance between the two points.
 */
double distSq(int x1, int y1, int x2, int y2) {
    long long dx = x2 - x1;
    long long dy = y2 - y1;
    return (double)(dx * dx + dy * dy);
}

/**
 * @brief Checks if three given points form a right-angled triangle.
 *
 * This function calculates the square of the lengths of the three sides formed
 * by the points and then checks if they satisfy the Pythagorean theorem (a^2 + b^2 = c^2).
 *
 * @param x1 The x-coordinate of the first vertex.
 * @param y1 The y-coordinate of the first vertex.
 * @param x2 The x-coordinate of the second vertex.
 * @param y2 The y-coordinate of the second vertex.
 * @param x3 The x-coordinate of the third vertex.
 * @param y3 The y-coordinate of the third vertex.
 * @return 1 if the points form a right-angled triangle, 0 otherwise.
 */
int isRightAngled(int x1, int y1, int x2, int y2, int x3, int y3) {
    // Calculate the square of the lengths of the three sides
    double d1_sq = distSq(x1, y1, x2, y2);
    double d2_sq = distSq(x2, y2, x3, y3);
    double d3_sq = distSq(x3, y3, x1, y1);

    // Check for collinearity or identical points. If any side has zero length,
    // the points do not form a triangle.
    if (d1_sq == 0 || d2_sq == 0 || d3_sq == 0) {
        return 0;
    }

    // Check if the Pythagorean theorem holds true for any combination of sides.
    // We compare floating-point numbers, but since the inputs are integers,
    // the squared distances will be exact integers, so direct comparison is safe.
    if ((d1_sq + d2_sq == d3_sq) ||
        (d1_sq + d3_sq == d2_sq) ||
        (d2_sq + d3_sq == d1_sq)) {
        return 1; // It is a right-angled triangle
    }

    return 0; // It is not a right-angled triangle
}

