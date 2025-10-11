import math

def check_solution_line(name, m, c, point_to_check, line1_m, line1_c, line2_m, line2_c):
    """Checks a single non-vertical solution line."""
    print(f"--- Checking Solution: {name} ---")
    px, py = point_to_check

    # 1. Check if the line passes through the point (2, 3)
    # Equation is y = mx + c. Let's see if (px, py) fits.
    if not math.isclose(py, m * px + c):
        print(f"  FAIL: Line does not pass through {point_to_check}.")
    else:
            print(f"  PASS: Line passes through {point_to_check}.")

    # 2. Find intersection with the first parallel line (y = -2x + 3)
    # mx + c = -2x + 3  => (m+2)x = 3-c
    x1 = (3 - c) / (m + 2)
    y1 = m * x1 + c
    print(f"  Intersection with first line: ({x1:.2f}, {y1:.2f})")

    # 3. Find intersection with the second parallel line (y = -2x + 5)
    # mx + c = -2x + 5 => (m+2)x = 5-c
    x2 = (5 - c) / (m + 2)
    y2 = m * x2 + c
    print(f"  Intersection with second line: ({x2:.2f}, {y2:.2f})")

    # 4. Calculate the distance between intersection points
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"  Calculated intercept distance: {distance:.4f}")

    # 5. Verify the distance
    if math.isclose(distance, 2.0):
        print("  PASS: Intercept length is 2.\n")
    else:
        print("  FAIL: Intercept length is not 2.\n")


def check_vertical_line(name, x_val, point_to_check, line1_m, line1_c, line2_m, line2_c):
    """Checks a single vertical solution line."""
    print(f"--- Checking Solution: {name} ---")
    px, py = point_to_check
    
    # 1. Check if the line passes through the point (2, 3)
    if not math.isclose(px, x_val):
        print(f"  FAIL: Line does not pass through {point_to_check}.")
        return
        
    print(f"  PASS: Line passes through {point_to_check}.")
    
    # 2. Find intersections by substituting x = x_val
    y1 = line1_m * x_val + line1_c
    y2 = line2_m * x_val + line2_c
    print(f"  Intersection with first line: ({x_val:.2f}, {y1:.2f})")
    print(f"  Intersection with second line: ({x_val:.2f}, {y2:.2f})")

    # 3. Calculate distance (it's just the difference in y-values)
    distance = abs(y2 - y1)
    print(f"  Calculated intercept distance: {distance:.4f}")
    
    # 4. Verify the distance
    if math.isclose(distance, 2.0):
        print("  PASS: Intercept length is 2.\n")
    else:
        print("  FAIL: Intercept length is not 2.\n")


if __name__ == '__main__':
    # --- Problem Setup ---
    # The point the line must pass through
    point = (2, 3)
    
    # The parallel lines in y = mx + c form
    # y + 2x = 3  =>  y = -2x + 3
    # y + 2x = 5  =>  y = -2x + 5
    m_parallel = -2
    c1 = 3
    c2 = 5

    # --- Verification ---
    
    # Solution 1: 3x + 4y = 18  =>  4y = -3x + 18  => y = -0.75x + 4.5
    check_solution_line(
        name="3x + 4y = 18", 
        m=-0.75, 
        c=4.5, 
        point_to_check=point,
        line1_m=m_parallel, line1_c=c1,
        line2_m=m_parallel, line2_c=c2
    )
    
    # Solution 2: x = 2 (a vertical line)
    check_vertical_line(
        name="x = 2",
        x_val=2,
        point_to_check=point,
        line1_m=m_parallel, line1_c=c1,
        line2_m=m_parallel, line2_c=c2
    )
