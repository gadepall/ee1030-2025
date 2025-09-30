#include <math.h>
#include "matfun.h"

double semi_major ( double e , double D ){
    return D / ( 2.0 * e );
}

double semi_minor ( double e , double D ){
    double a = semi_major ( e , D );
    return a * sqrt ( 1.0 - e * e );
}

double focal_distance ( double e , double D ){
    return semi_major ( e , D ) * e;
}

double latus_rectum ( double e , double D ){
    return D * ( 1.0 - e * e ) / e;
}

void ellipse_points(double a , double b ,int    N ,double *x ,double *y){
    for ( int i = 0 ; i < N ; ++i )
    {
        double t = 2.0 * M_PI * i / N;
        x [ i ] = a * cos ( t );
        y [ i ] = b * sin ( t );
    }
}
