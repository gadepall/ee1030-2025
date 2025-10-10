
// code.c
#define NUM_POINTS 4

void get_points(double* arr) {
    double pts[NUM_POINTS][3] = {
        {1, -1, 2},
        {3,  4, -2},
        {0,  3,  2},
        {3,  5,  6}
    };
    for (int i = 0; i < NUM_POINTS; ++i)
        for (int j = 0; j < 3; ++j)
            arr[i*3 + j] = pts[i][j];
}

void get_dir_vectors(double* v1, double* v2) {
    v1[0] = 3 - 1;
    v1[1] = 4 - (-1);
    v1[2] = -2 - 2;
    v2[0] = 3 - 0;
    v2[1] = 5 - 3;
    v2[2] = 6 - 2;
}

int check_perpendicular() {
    double v1[3], v2[3];
    get_dir_vectors(v1, v2);
    double dot = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
    return dot == 0 ? 1 : 0;
}

