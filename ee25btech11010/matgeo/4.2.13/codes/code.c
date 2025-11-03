typedef struct {
    double nx;
    double ny;
    double dx;
    double dy;
} LineVectors;

LineVectors find_vectors(double a, double b, double c) {
    LineVectors result;
    result.nx = a;
    result.ny = b;
    result.dx = -b;
    result.dy = a;
    return result;
}
