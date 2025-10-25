#ifndef MATFUN_H
#define MATFUN_H

#ifdef __cplusplus
extern "C" {
#endif

// Check validity of edge: returns 1 for valid, else 0
int check_line_validity(double r0[3], double d[3]);

// Prepare points on line for plotting
void prepare_line_points(double r0[3], double d[3], double t_start, double t_end, int num_points, double *output);

#ifdef __cplusplus
}
#endif

#endif

