// matfun.h
#ifndef MATFUN_H
#define MATFUN_H

#ifdef __cplusplus
extern "C" {
#endif

void foot_of_perpendicular(const double *P, const double *Q, const double *R, double *foot);
void orthocenter(const double *A, const double *B, const double *C, double *O);

#ifdef __cplusplus
}
#endif

#endif

