#include <stdio.h>


void trisect_points(double ax, double ay, double bx, double by,
		double *px, double *py, double *qx, double *qy)
                    {
                         
                            *px = (1 * bx + 2 * ax) / 3.0;
                                *py = (1 * by + 2 * ay) / 3.0;
                                      *qx = (2 * bx + 1 * ax) / 3.0;
                                           *qy = (2 * by + 1 * ay) / 3.0;
                                          }
