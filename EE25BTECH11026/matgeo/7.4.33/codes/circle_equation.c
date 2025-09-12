#include <stdio.h>
#include <math.h>

// structure for 2D point
typedef struct {
    double x, y;
} Point;

// normalize vector
void normalize(double *x, double *y) {
    double norm = sqrt((*x)*(*x) + (*y)*(*y));
    if (norm > 1e-12) {
        *x /= norm;
        *y /= norm;
    }
}

// rotate by theta
Point rotate(Point v, double theta) {
    Point r;
    double c = cos(theta), s = sin(theta);
    r.x = c*v.x - s*v.y;
    r.y = s*v.x + c*v.y;
    return r;
}

// solve 2x2 system
Point intersect(double a1,double b1,double c1, double a2,double b2,double c2) {
    double det = a1*b2 - a2*b1;
    Point P;
    P.x = (b1*c2 - b2*c1)/det;
    P.y = (c1*a2 - c2*a1)/det;
    return P;
}

// main solver: fills arrays with results
void solve_geometry(double *results) {
    // Given: line PQ: sqrt(3)x + y - 6 = 0
    double a = sqrt(3.0), b = 1.0, c = -6.0;
    Point D = {3*sqrt(3.0)/2.0, 1.5};
    double r = 1.0;

    // unit normal
    double nx=a, ny=b;
    normalize(&nx,&ny);

    // candidate centers
    Point C1 = {D.x + r*nx, D.y + r*ny};
    Point C2 = {D.x - r*nx, D.y - r*ny};

    // check side with origin
    double origin_side = a*0 + b*0 + c;
    double side1 = a*C1.x + b*C1.y + c;
    Point O = (side1*origin_side > 0) ? C1 : C2;

    // tangency vectors
    Point vD = {D.x - O.x, D.y - O.y};
    Point vE = rotate(vD, 2*M_PI/3.0);
    Point vF = rotate(vD, -2*M_PI/3.0);

    Point E = {O.x + vE.x, O.y + vE.y};
    Point F = {O.x + vF.x, O.y + vF.y};

    // tangent lines: ax+by+c=0
    double cPQ = -(vD.x*D.x + vD.y*D.y);
    double cQR = -(vE.x*E.x + vE.y*E.y);
    double cRP = -(vF.x*F.x + vF.y*F.y);

    // vertices
    Point P = intersect(vD.x, vD.y, cPQ, vF.x, vF.y, cRP);
    Point Q = intersect(vD.x, vD.y, cPQ, vE.x, vE.y, cQR);
    Point R = intersect(vE.x, vE.y, cQR, vF.x, vF.y, cRP);

    // fill results array (order: O,D,E,F,P,Q,R)
    results[0]=O.x; results[1]=O.y;
    results[2]=D.x; results[3]=D.y;
    results[4]=E.x; results[5]=E.y;
    results[6]=F.x; results[7]=F.y;
    results[8]=P.x; results[9]=P.y;
    results[10]=Q.x; results[11]=Q.y;
    results[12]=R.x; results[13]=R.y;
}

