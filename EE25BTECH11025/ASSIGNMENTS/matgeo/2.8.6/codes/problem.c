#include<stdio.h>
#include<math.h>

typedef struct { double x, y; } Point;
typedef struct { double a, b, c; } Line;

static Point stored_point = {1.0, 2.0};
static Line  stored_line  = {1.0, -3.0, 4.0};

void get_point(double* x, double* y){ if(x)*x=stored_point.x; if(y)*y=stored_point.y; }
void get_line(double* a,double* b,double* c){ if(a)*a=stored_line.a; if(b)*b=stored_line.b; if(c)*c=stored_line.c; }

void reflect_point_across_line(double x0, double y0,
                               double a, double b, double c,
                               double* xr, double* yr)
{
    double denom = a*a + b*b;
    double t = (a*x0 + b*y0 + c) / denom;
    if(xr) *xr = x0 - 2*a*t;
    if(yr) *yr = y0 - 2*b*t;
}

void reflect_stored(double* xr, double* yr){
    reflect_point_across_line(stored_point.x, stored_point.y,
                              stored_line.a, stored_line.b, stored_line.c,
                              xr, yr);
}

