typedef struct {
    double x, y, z;
} Vector3D;

void find_normal_vector_lib(Vector3D p, Vector3D q, Vector3D r, Vector3D* normal_out) {
    Vector3D vec_pq = {q.x - p.x, q.y - p.y, q.z - p.z};
    Vector3D vec_pr = {r.x - p.x, r.y - p.y, r.z - p.z};
    
    normal_out->x = (vec_pq.y * vec_pr.z) - (vec_pq.z * vec_pr.y);
    normal_out->y = (vec_pq.z * vec_pr.x) - (vec_pq.x * vec_pr.z);
    normal_out->z = (vec_pq.x * vec_pr.y) - (vec_pq.y * vec_pr.x);
}
