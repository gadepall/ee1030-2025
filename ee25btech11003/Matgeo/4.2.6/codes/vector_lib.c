/**
 * @brief Calculates the normal and direction vectors of a line ax + by + c = 0.
 *
 * @param a The coefficient of x.
 * @param b The coefficient of y.
 * @param normal_vec A float array of size 2 to store the normal vector <x, y>.
 * @param direction_vec A float array of size 2 to store the direction vector <x, y>.
 */
void get_line_vectors(float a, float b, float normal_vec[], float direction_vec[]) {
    // The normal vector is <a, b>.
    normal_vec[0] = a;
    normal_vec[1] = b;

    // The direction vector is perpendicular to the normal, so <-b, a>.
    direction_vec[0] = -b;
    direction_vec[1] = a;
}
