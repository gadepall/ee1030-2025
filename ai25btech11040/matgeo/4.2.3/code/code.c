/*
The matrix
0   1
-1  0
rotates a vector by 90 degrees in the clockwise direction.

Therefore, a point [[x], [y]] when multiplied by this matrix results in a point [[y], [-x]], which is the original point rotated by 90 degrees clockwise.
*/

double direction_vec_x(double x, double y){
    return y;
}

double direction_vec_y(double x, double y){
    return -x;
}