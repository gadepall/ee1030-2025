#include <stdlib.h> // Required for malloc and free

// The same Point structure
typedef struct {
    float x;
    float y;
} Point;

/**
 * @brief Generates points on a line segment.
 * * @param A The starting point of the segment.
 * @param B The ending point of the segment.
 * @param num_steps The number of intervals to divide the line into.
 * @param result_array A pointer that will be set to the newly allocated array of points.
 * @param count A pointer that will be set to the number of points generated.
 */
void generate_points_on_line(Point A, Point B, int num_steps, Point** result_array, int* count) {
    // Total number of points is num_steps + 1 (to include both endpoints)
    int total_points = num_steps + 1;
    
    // Allocate memory for the array of points
    Point* points = (Point*)malloc(total_points * sizeof(Point));
    if (points == NULL) {
        // Failed to allocate memory
        *result_array = NULL;
        *count = 0;
        return;
    }

    // Loop and calculate each point using the parametric form
    for (int i = 0; i <= num_steps; i++) {
        float t = (float)i / num_steps;
        points[i].x = A.x + t * (B.x - A.x);
        points[i].y = A.y + t * (B.y - A.y);
    }
    
    // Return the results by modifying the pointers passed as arguments
    *result_array = points;
    *count = total_points;
}

/**
 * @brief Frees the memory allocated by generate_points_on_line.
 * * @param points_array The pointer to the memory block to be freed.
 */
void free_points_memory(Point* points_array) {
    free(points_array);
}

