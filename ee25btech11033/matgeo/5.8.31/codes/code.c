#include <stdio.h>
void calculate_angles(double* angle_A, double* angle_B, double* angle_C) {
    /*
      The problem is defined by the following system of equations:
      1) A + B + C = 180
      2) C = 3B
      3) 3B = 2(A + B)

      Solving the system:
      From (3): 3B = 2A + 2B  =>  B = 2A
      Substitute B into (2): C = 3 * (2A)  =>  C = 6A
      Substitute B and C into (1): A + 2A + 6A = 180  =>  9A = 180  =>  A = 20
      
      Therefore:
      A = 20 degrees
      B = 2 * 20 = 40 degrees
      C = 6 * 20 = 120 degrees
    */
    *angle_A = 20.0;
    *angle_B = 40.0;
    *angle_C = 120.0;
}
