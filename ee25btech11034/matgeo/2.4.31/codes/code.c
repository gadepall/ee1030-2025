#include <math.h>

// Define a structure to represent a 2D point
typedef struct {
    double x;
    double y;
} Point;

/**
 * @brief Checks if a point A lies on the perpendicular bisector of segment PQ.
 *
 * @param A The point to check.
 * @param P The first endpoint of the line segment.
 * @param Q The second endpoint of the line segment.
 * @return int 1 if A is on the bisector (true), 0 otherwise (false).
 */
int checkPerpendicularBisector(Point A, Point P, Point Q) {
    double dist_AP_sq = pow(P.x - A.x, 2) + pow(P.y - A.y, 2);
    double dist_AQ_sq = pow(Q.x - A.x, 2) + pow(Q.y - A.y, 2);
    const double TOLERANCE = 1e-9;
    
    if (fabs(dist_AP_sq - dist_AQ_sq) < TOLERANCE) {
        return 1; // Represents true
    } else {
        return 0; // Represents false
    }
}

/**
 * @brief Generates points along a line segment and stores them in an array.
 *
 * @param p1 The starting point of the segment.
 * @param p2 The ending point of the segment.
 * @param numPoints The total number of points to generate.
 * @param out_points A pointer to an array of Points to be filled with the results.
 */
void generateLinePoints(Point p1, Point p2, int numPoints, Point* out_points) {
    if (numPoints < 2) {
        // Handle case with insufficient points gracefully
        if (numPoints == 1) {
            out_points[0] = p1;
        }
        return;
    }

    for (int i = 0; i < numPoints; i++) {
        // 't' is the parameter that goes from 0.0 to 1.0
        double t = (double)i / (numPoints - 1);

        // Parametric equation for the line
        out_points[i].x = (1 - t) * p1.x + t * p2.x;
        out_points[i].y = (1 - t) * p1.y + t * p2.y;
    }
}
