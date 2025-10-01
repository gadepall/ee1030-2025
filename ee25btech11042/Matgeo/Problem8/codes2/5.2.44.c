

void get_conic_data(double* data_out) {
    // Hyperbola 1: V1=[[4,0],[0,-4]], u1=[-6,4]
    data_out[0] = 4.0;  data_out[1] = 0.0;
    data_out[2] = 0.0;  data_out[3] = -4.0;
    data_out[4] = -6.0; data_out[5] = 4.0;

    // Hyperbola 2: V2=[[-2,0],[0,2]], u2=[-5,10]
    data_out[6] = -2.0; data_out[7] = 0.0;
    data_out[8] = 0.0;  data_out[9] = 2.0;
    data_out[10] = -5.0; data_out[11] = 10.0;

    // Solution Point: [3, 2]
    data_out[12] = 3.0; data_out[13] = 2.0;
}

