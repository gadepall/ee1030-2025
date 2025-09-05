#include <stdio.h>
#include <math.h>

// structure for point
typedef struct {
    int x, y;
} Point;

// function to compute vector dot product
int dot(Point a, Point b) {
    return a.x * b.x + a.y * b.y;
}

// function to compute vector length squared
int lengthSq(Point a) {
    return a.x * a.x + a.y * a.y;
}

// function to subtract two points (vector)
Point subtract(Point a, Point b) {
    Point res = {a.x - b.x, a.y - b.y};
    return res;
}

void findQuadrilateral(Point A, Point B, Point C, Point D) {
    Point AB = subtract(B, A);
    Point BC = subtract(C, B);
    Point CD = subtract(D, C);
    Point DA = subtract(A, D);

    // check parallelogram condition: AB = -CD and BC = -DA
    int isParallelogram = (AB.x == -CD.x && AB.y == -CD.y &&
                           BC.x == -DA.x && BC.y == -DA.y);

    if (!isParallelogram) {
        printf("The points do not form a parallelogram (general quadrilateral).\n");
        return;
    }

    int AB_len = lengthSq(AB);
    int BC_len = lengthSq(BC);
    int CD_len = lengthSq(CD);
    int DA_len = lengthSq(DA);

    // check right angle using dot product
    if (dot(AB, BC) == 0) {
        if (AB_len == BC_len) {
            printf("The quadrilateral is a Square.\n");
        } else {
            printf("The quadrilateral is a Rectangle.\n");
        }
    } else {
        // if all sides equal but not right angle -> rhombus
        if (AB_len == BC_len && BC_len == CD_len && CD_len == DA_len) {
            printf("The quadrilateral is a Rhombus.\n");
        } else {
            printf("The quadrilateral is a Parallelogram.\n");
        }
    }
}