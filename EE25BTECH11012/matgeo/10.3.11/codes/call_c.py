from ctypes import c_double

def main():
    # --- Given Problem Data ---
    x1 = c_double(1.0)
    y1 = c_double(1.0)

    # --- Calculations ---
    m_tangent = c_double(-x1.value)  # dy/dx = -x

    if m_tangent.value == 0:
        print(f"The equation of the normal line is: x = {x1.value:.2f}")
    else:
        m_normal = c_double(-1.0 / m_tangent.value)
        c_intercept = c_double(y1.value - m_normal.value * x1.value)

        # --- Print the Final Answer ---
        print("The equation of the normal line is: ", end="")

        if m_normal.value == 1 and c_intercept.value == 0:
            print("y = x")
        elif m_normal.value == -1 and c_intercept.value == 0:
            print("y = -x")
        else:
            print(f"y = {m_normal.value:.2f}x", end="")
            if c_intercept.value > 0:
                print(f" + {c_intercept.value:.2f}")
            elif c_intercept.value < 0:
                print(f" - {abs(c_intercept.value):.2f}")
            else:
                print()

if __name__ == "__main__":
    main()
