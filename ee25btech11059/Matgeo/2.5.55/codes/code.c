#include <stdio.h>
#include <math.h>

#define MAX_POINTS 10000
#define STEP 1.0
#define TOL 0.5  // tolerance
#define SIDE_LENGTH 12.0

typedef struct {
    double x, y, z;
} Point;

double dist2(Point a, Point b) {
    return (a.x - b.x)*(a.x - b.x) +
           (a.y - b.y)*(a.y - b.y) +
           (a.z - b.z)*(a.z - b.z);
}

void solve_vectors() {
    Point P = {1, 2, 3};
    Point Q = {4, 2, 7};

    Point S[MAX_POINTS];
    Point T[MAX_POINTS];
    int s_count = 0, t_count = 0;

    for (double x = -10; x <= 10; x += STEP) {
        for (double y = -10; y <= 10; y += STEP) {
            for (double z = -10; z <= 10; z += STEP) {
                Point A = {x, y, z};
                double lhs = dist2(A, P);
                double rhs = dist2(A, Q);
                double d = lhs - rhs;

                if (fabs(d - 50.0) < TOL && s_count < MAX_POINTS) {
                    S[s_count++] = A;
                } else if (fabs(-d - 50.0) < TOL && t_count < MAX_POINTS) {
                    T[t_count++] = A;
                }
            }
        }
    }

    printf("Found %d points on Set S and %d points on Set T.\n", s_count, t_count);

    for (int i = 0; i < s_count; i++) {
        for (int j = 0; j < t_count; j++) {
            double d = sqrt(dist2(S[i], T[j]));
            if (fabs(d - SIDE_LENGTH) < TOL) {
                printf("Found square side length %.2f\n", d);
                printf("S-point: (%.2f, %.2f, %.2f)\n", S[i].x, S[i].y, S[i].z);
                printf("T-point: (%.2f, %.2f, %.2f)\n", T[j].x, T[j].y, T[j].z);
                return;
            }
        }
    }
    printf("No square found.\n");
}
