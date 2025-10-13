import ctypes
import math

# Define the Point struct using ctypes
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

def main():
    # Let the starting point P be the origin
    p = Point(0.0, 0.0)
    current_pos = Point(0.0, 0.0)

    print("Simulating Phani's journey...")
    print(f"Start at P: ({current_pos.x:.1f}, {current_pos.y:.1f})")

    # 1. Goes North for 3 km
    current_pos.y += 3.0
    print(f"1. After moving North 3 km: ({current_pos.x:.1f}, {current_pos.y:.1f})")

    # 2. Then East for 4 km to reach point Q
    current_pos.x += 4.0
    q = Point(current_pos.x, current_pos.y)
    print(f"2. After moving East 4 km to Q: ({current_pos.x:.1f}, {current_pos.y:.1f})")

    # 3. Turns to face point P and goes 15 km
    vec_to_p_x = p.x - q.x  # -4.0
    vec_to_p_y = p.y - q.y  # -3.0

    dist_qp = math.sqrt(vec_to_p_x**2 + vec_to_p_y**2)

    unit_vec_x = vec_to_p_x / dist_qp
    unit_vec_y = vec_to_p_y / dist_qp

    current_pos.x += 15.0 * unit_vec_x
    current_pos.y += 15.0 * unit_vec_y
    print(f"3. After moving 15 km towards P: ({current_pos.x:.1f}, {current_pos.y:.1f})")

    # 4. Then goes North for 6 km
    current_pos.y += 6.0
    print(f"4. After moving North 6 km (Final Position): ({current_pos.x:.1f}, {current_pos.y:.1f})\n")

    # Question 1: Distance from point P
    final_distance = math.sqrt((current_pos.x - p.x)**2 + (current_pos.y - p.y)**2)

    # Question 2: Direction to reach point P
    dir_to_p_x = p.x - current_pos.x

    print("Final Answer:")
    print(f"Distance from start point P: {final_distance:.0f} km")

    if dir_to_p_x > 0:
        print("Direction to reach point P: East")
    elif dir_to_p_x < 0:
        print("Direction to reach point P: West")
    else:
        print("Direction to reach point P: Same line")

    print("This corresponds to option a) 8 km, East.")

if __name__ == "__main__":
    main()