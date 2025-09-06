#include <stdio.h>
#include <math.h>

/* 3D point and vector types */
typedef struct { double x, y, z; } Point3D;
typedef struct { double x, y, z; } Vector3D;

/* Subtract two points (p1 - p2) -> vector */
Vector3D subtract_points(Point3D p1, Point3D p2) {
    Vector3D r;
    r.x = p1.x - p2.x;
    r.y = p1.y - p2.y;
    r.z = p1.z - p2.z;
    return r;
}

/* Cross product v1 × v2 */
Vector3D cross_product(Vector3D v1, Vector3D v2) {
    Vector3D r;
    r.x = v1.y * v2.z - v1.z * v2.y;
    r.y = v1.z * v2.x - v1.x * v2.z;
    r.z = v1.x * v2.y - v1.y * v2.x;
    return r;
}

/* Vector magnitude */
double magnitude(Vector3D v) {
    return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}

/* Plane normal from three points: n = (B - A) × (C - A) */
Vector3D find_plane_normal(Point3D A, Point3D B, Point3D C) {
    Vector3D AB = subtract_points(B, A);
    Vector3D AC = subtract_points(C, A);
    return cross_product(AB, AC);
}

/* Plane constant k in: n.x*x + n.y*y + n.z*z = k, using a point on plane */
double find_plane_constant(Point3D A, Vector3D n) {
    return n.x * A.x + n.y * A.y + n.z * A.z;
}

/* Foot of perpendicular from P to plane with normal n and constant k */
Point3D find_foot_of_perpendicular(Point3D P, Vector3D n, double k) {
    /* Line: L(t) = P + t n; impose n · L(t) = k to solve for t */
    double num = k - (n.x * P.x + n.y * P.y + n.z * P.z);
    double den = n.x * n.x + n.y * n.y + n.z * n.z;
    double t = num / den;

    Point3D Q;
    Q.x = P.x + t * n.x;
    Q.y = P.y + t * n.y;
    Q.z = P.z + t * n.z;
    return Q;
}

/* Distance between two points */
double distance_between_points(Point3D p1, Point3D p2) {
    Vector3D d = subtract_points(p1, p2);
    return magnitude(d);
}

/* Save points to points.dat in text format */
void save_points_to_file(Point3D A, Point3D B, Point3D C, Point3D P, Point3D Q) {
    FILE *fp = fopen("points.dat", "w");
    if (!fp) return;
    fprintf(fp, "A %.10f %.10f %.10f\n", A.x, A.y, A.z);
    fprintf(fp, "B %.10f %.10f %.10f\n", B.x, B.y, B.z);
    fprintf(fp, "C %.10f %.10f %.10f\n", C.x, C.y, C.z);
    fprintf(fp, "P %.10f %.10f %.10f\n", P.x, P.y, P.z);
    fprintf(fp, "Q %.10f %.10f %.10f\n", Q.x, Q.y, Q.z);
    fclose(fp);
}

/* Solve distance from P to plane ABC, return distance, write Q via pointer, and save A,B,C,P,Q to points.dat */
double solve_point_to_plane_distance(Point3D A, Point3D B, Point3D C, Point3D P, Point3D *Q_out) {
    Vector3D n = find_plane_normal(A, B, C);
    double k = find_plane_constant(A, n);
    Point3D Q = find_foot_of_perpendicular(P, n, k);
    if (Q_out) *Q_out = Q;
    save_points_to_file(A, B, C, P, Q);
    return distance_between_points(P, Q);
}

/* Convenience function with the exact problem data from the PDF:
   A(3,-1,2), B(5,2,4), C(-1,-1,6), P(6,5,9).
   Calls the solver, writes points.dat, and returns the distance. */
double generate_points_and_save(void) {
    Point3D A = { 3.0, -1.0, 2.0 };
    Point3D B = { 5.0,  2.0, 4.0 };
    Point3D C = {-1.0, -1.0, 6.0 };
    Point3D P = { 6.0,  5.0, 9.0 };
    Point3D Q;
    return solve_point_to_plane_distance(A, B, C, P, &Q);
}

