// File: vector_ops.c

float check_perpendicularity(float ax, float ay, float az, float bx, float by, float bz) {
    // Calculate p = a + b
    float px = ax + bx;
    float py = ay + by;
    float pz = az + bz;

    // Calculate q = a - b
    float qx = ax - bx;
    float qy = ay - by;
    float qz = az - bz;

    // Return the dot product of p and q
    return (px * qx) + (py * qy) + (pz * qz);
}