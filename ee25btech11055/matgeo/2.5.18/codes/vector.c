void vec_sum(const double* vec1, const double* vec2, double* sum) {
    sum[0] = vec1[0] + vec2[0];
    sum[1] = vec1[1] + vec2[1];
    sum[2] = vec1[2] + vec2[2];
}
void vec_diff(const double* vec1, const double* vec2, double* diff) {
    diff[0] = vec1[0] - vec2[0];
    diff[1] = vec1[1] - vec2[1];
    diff[2] = vec1[2] - vec2[2];
}