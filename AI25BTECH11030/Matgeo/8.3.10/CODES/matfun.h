#ifndef MATFUN_H
#define MATFUN_H

double semi_major     ( double e , double D );
double semi_minor     ( double e , double D );
double focal_distance ( double e , double D );
double latus_rectum   ( double e , double D );

void ellipse_points(double a , double b ,int N , double *x , double *y);

#endif
