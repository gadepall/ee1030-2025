
void calculate_parallelogram_coords(double* out_coords) {
    // Given vertices
    double Ax = 6.0, Ay = 1.0;
    double Bx = 8.0, By = 2.0;
    double Cx = 9.0, Cy = 4.0;
    
    double Dx = Ax - Bx + Cx;
    double Dy = Ay - By + Cy;

    double Ex = (Dx + Cx) / 2.0;
    double Ey = (Dy + Cy) / 2.0;
  
    out_coords[0] = Ax; out_coords[1] = Ay;
    out_coords[2] = Bx; out_coords[3] = By;
    out_coords[4] = Cx; out_coords[5] = Cy;
    out_coords[6] = Dx; out_coords[7] = Dy;
    out_coords[8] = Ex; out_coords[9] = Ey;
}