void find_p_prime(double p_x, double p_y, double c_x, double c_y, double* p_prime_coords) {
    // Calculate the x-coordinate of P'
    p_prime_coords[0] = 2.0 * c_x - p_x;

    // Calculate the y-coordinate of P'
    p_prime_coords[1] = 2.0 * c_y - p_y;
}
