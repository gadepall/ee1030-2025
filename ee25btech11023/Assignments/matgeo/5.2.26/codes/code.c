 
void get_system_coeffs(double* out_coeffs) {
 
    double a = 3.0;
    double b = 2.0;
   
    out_coeffs[0] = b;
    out_coeffs[1] = -a;
    out_coeffs[2] = a;
    out_coeffs[3] = b;
 
    out_coeffs[4] = 0;
    out_coeffs[5] = a*a + b*b;
 
    out_coeffs[6] = a;
    out_coeffs[7] = b;
}