#ifndef CONIC_SOLVER_H
#define CONIC_SOLVER_H

typedef struct {
    double x1, y1;
    double x2, y2;
} Intersection;

Intersection solve_conic(double p);

#endif

