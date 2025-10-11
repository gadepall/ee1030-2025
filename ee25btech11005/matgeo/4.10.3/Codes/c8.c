void plane_point(double x, double y, double plane_n[3], double constant, double out[3]) {
    out[0] = x;
    out[1] = y;
    out[2] = (constant - plane_n[0]*x - plane_n[1]*y) / plane_n[2];
}

