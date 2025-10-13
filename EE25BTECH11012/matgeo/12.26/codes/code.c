#include <stdio.h>
#include <math.h>

// A struct to represent a point with x and y coordinates
typedef struct {
    double x;
    double y;
} Point;

int main() {
    // Let the starting point P be the origin
    Point p = {0.0, 0.0};
    Point current_pos = {0.0, 0.0};

    printf("Simulating Phani's journey...\n");
    printf("Start at P: (%.1f, %.1f)\n", current_pos.x, current_pos.y);

    // 1. Goes North for 3 km
    current_pos.y += 3.0;
    printf("1. After moving North 3 km: (%.1f, %.1f)\n", current_pos.x, current_pos.y);

    // 2. Then East for 4 km to reach point Q
    current_pos.x += 4.0;
    Point q = current_pos;
    printf("2. After moving East 4 km to Q: (%.1f, %.1f)\n", current_pos.x, current_pos.y);

    // 3. Turns to face point P and goes 15 km
    // Vector from current position (Q) towards P
    double vec_to_p_x = p.x - q.x; // 0 - 4 = -4
    double vec_to_p_y = p.y - q.y; // 0 - 3 = -3

    // The distance between Q and P (magnitude of the vector)
    double dist_qp = sqrt(vec_to_p_x * vec_to_p_x + vec_to_p_y * vec_to_p_y);

    // Create a unit vector for the direction
    double unit_vec_x = vec_to_p_x / dist_qp;
    double unit_vec_y = vec_to_p_y / dist_qp;

    // Move 15 km along this direction
    current_pos.x += 15.0 * unit_vec_x;
    current_pos.y += 15.0 * unit_vec_y;
    printf("3. After moving 15 km towards P: (%.1f, %.1f)\n", current_pos.x, current_pos.y);

    // 4. Then goes North for 6 km
    current_pos.y += 6.0;
    printf("4. After moving North 6 km (Final Position): (%.1f, %.1f)\n\n", current_pos.x, current_pos.y);

    // Question 1: How far is she from point P?
    double final_distance = sqrt(pow(current_pos.x - p.x, 2) + pow(current_pos.y - p.y, 2));

    // Question 2: In which direction should she go to reach point P?
    // Vector from her final position back to P
    double dir_to_p_x = p.x - current_pos.x; // 0 - (-8) = 8

    printf("Final Answer:\n");
    printf("Distance from start point P: %.0f km\n", final_distance);
    printf("Direction to reach point P: ");

    if (dir_to_p_x > 0) {
        printf("East\n");
    } else if (dir_to_p_x < 0) {
        printf("West\n");
    } // simplified for this problem

    printf("This corresponds to option a) 8 km, East.\n");
    return 0;
}