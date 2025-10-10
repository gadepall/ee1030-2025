void plane_from_points(double P1[3], double P2[3], double P3[3], double coeff[4]) {
    coeff[0] = (P2[1]-P1[1])*(P3[2]-P1[2]) - (P2[2]-P1[2])*(P3[1]-P1[1]); // a
    coeff[1] = (P2[2]-P1[2])*(P3[0]-P1[0]) - (P2[0]-P1[0])*(P3[2]-P1[2]); // b
    coeff[2] = (P2[0]-P1[0])*(P3[1]-P1[1]) - (P2[1]-P1[1])*(P3[0]-P1[0]); // c
    coeff[3] = coeff[0]*P1[0] + coeff[1]*P1[1] + coeff[2]*P1[2];
}
void parallel_plane_through_point(double coeff[4], double Q[3], double coeff2[4]) {
    coeff2[0] = coeff[0];
    coeff2[1] = coeff[1];
    coeff2[2] = coeff[2];
    coeff2[3] = coeff[0]*Q[0] + coeff[1]*Q[1] + coeff[2]*Q[2];
}

