#include <stdio.h>
#include <math.h> 

typedef struct {
    float x, y, z;
} Vector3D;

Vector3D find_unit_vector(Vector3D P, Vector3D Q) {

    Vector3D PQ;
    PQ.x = Q.x - P.x;
    PQ.y = Q.y - P.y;
    PQ.z = Q.z - P.z;
    
    float magnitude = sqrtf(PQ.x * PQ.x + PQ.y * PQ.y + PQ.z * PQ.z);
   
    Vector3D unit_vector = {0.0f, 0.0f, 0.0f}; 

    
    if (magnitude > 0) {
        unit_vector.x = PQ.x / magnitude;
        unit_vector.y = PQ.y / magnitude;
        unit_vector.z = PQ.z / magnitude;
    }

    return unit_vector;
}


