void generate_plane_points(
    // Output params
    double* x_coords, double* y_coords, double* z_coords,
    // Grid params
    double x_min, double x_max, int x_steps,
    double y_min, double y_max, int y_steps,
    // Plane stuff
    double n1, double n2, double n3, double c) {
    
    double x_step_val = (x_max - x_min) / (x_steps - 1);
    double y_step_val = (y_max - y_min) / (y_steps - 1);
    int index = 0;

    for (int i = 0; i < x_steps; i++) {
        for (int j = 0; j < y_steps; j++) {
            double current_x = x_min + i * x_step_val;
            double current_y = y_min + j * y_step_val;
            double current_z;

            // Vertical plane check
            if ((c < 1e-9)&&(c > -1e-9)) {
                current_z = 0.0; 
            } else {
                current_z = (-n1 * current_x - n2 * current_y + c) / n3;
            }

            x_coords[index] = current_x;
            y_coords[index] = current_y;
            z_coords[index] = current_z;
            index++;
        }
    }
}