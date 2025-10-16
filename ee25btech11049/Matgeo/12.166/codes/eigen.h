#ifndef MATRIX_OPS_H
#define MATRIX_OPS_H

/*
 * This is the main function that will be called from Python.
 * It performs the verification checks seen in the output image.
 *
 * It calculates:
 * 1. Q * (R * x) -> stored in `q_rx_result`
 * 2. λ * (R * x) -> stored in `lambda_rx_result`
 * 3. Q * (R⁻¹ * x) -> stored in `q_rinvx_result`
 * 4. λ * (R⁻¹ * x) -> stored in `lambda_rinvx_result`
 *
 * Parameters:
 * Q, R, R_inv: Input matrices (flattened n x n arrays)
 * x: Input eigenvector (n-element array)
 * lambda: Input eigenvalue (scalar)
 * n: The dimension of the matrices (e.g., 3 for a 3x3 matrix)
 * ..._result: Output arrays where the results are stored
 */
void perform_verification(
    double* Q, double* R, double* R_inv, double* x, double lambda, int n,
    double* q_rx_result,
    double* lambda_rx_result,
    double* q_rinvx_result,
    double* lambda_rinvx_result
);

#endif // MATRIX_OPS_H

