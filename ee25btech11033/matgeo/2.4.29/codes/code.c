#include <stdio.h>
#include <math.h>
#include <stdlib.h>

typedef struct {
    double x;
    double y;
} Point;

typedef struct {
    int count;
    double solution1;
    double solution2;
} Solutions;


Solutions solveForA(Point A, double B_y, Point C) {
    Solutions result = {0, 0.0, 0.0};
    
    double P = 1.0;
    double Q = -(A.x + C.x);
    double R = (A.x * C.x) + (A.y - B_y) * (C.y - B_y);
    double discriminant = Q*Q - 4*P*R;

    if (discriminant < 0) {
        return result;
    }

    double a1 = (-Q + sqrt(discriminant)) / (2*P);
    double a2 = (-Q - sqrt(discriminant)) / (2*P);

    int a1_is_valid = !(a1 == A.x && B_y == A.y) && !(a1 == C.x && B_y == C.y);
    int a2_is_valid = !(a2 == A.x && B_y == A.y) && !(a2 == C.x && B_y == C.y);

    if (a1_is_valid) {
        result.solution1 = a1;
        result.count++;
    }
    
    if (discriminant > 1e-9 && a2_is_valid) {
        if (result.count == 0) {
            result.solution1 = a2;
        } else {
            result.solution2 = a2;
        }
        result.count++;
    }
    
    return result;
}

double getValidA() {
    Point A = {2.0, 9.0};
    Point C = {5.0, 5.0};
    double B_y = 5.0;
    
    Solutions solutions = solveForA(A, B_y, C);
    
    if (solutions.count > 0) {
        return solutions.solution1;
    }
    
    return 2.0;
}
