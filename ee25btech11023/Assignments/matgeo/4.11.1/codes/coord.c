 
void get_intersection_data(double* out_data) {
    double point_a[3] = {1.0, -4.0, -4.0};
  
    double dir_d[3] = {3.0, 7.0, 2.0};

    double lambda = 2.0;

    double Px = point_a[0] + lambda * dir_d[0]; 
    double Py = point_a[1] + lambda * dir_d[1]; 
    double Pz = point_a[2] + lambda * dir_d[2]; 
 
    out_data[0] = Px; 
    out_data[1] = Py; 
    out_data[2] = Pz;
    out_data[3] = point_a[0];
    out_data[4] = point_a[1]; 
    out_data[5] = point_a[2];
    out_data[6] = dir_d[0]; 
    out_data[7] = dir_d[1]; 
    out_data[8] = dir_d[2];
}