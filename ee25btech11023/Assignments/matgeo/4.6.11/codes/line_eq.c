

void get_line_vectors(double* out_data) {
 
    double point_a[3] = {1.0, -3.0, 2.0};
     
    double dir_b[3] = {1.0, 1.0, 2.0};
    
    out_data[0] = point_a[0];
    out_data[1] = point_a[1];
    out_data[2] = point_a[2];
    
    out_data[3] = dir_b[0];
    out_data[4] = dir_b[1];
    out_data[5] = dir_b[2];
}