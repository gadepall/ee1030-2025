import ctypes

def main():
    narayan_age = ctypes.c_int()
    daughter_age = ctypes.c_int()
    solution_found = ctypes.c_int(0)

    for narayan in range(1, 151):
        for daughter in range(1, narayan):
            narayan_age.value = narayan
            daughter_age.value = daughter

            # Condition 1
            is_condition1_met = (narayan_age.value - 7) == 7 * (daughter_age.value - 7)

            # Condition 2
            is_condition2_met = (narayan_age.value + 3) == 3 * (daughter_age.value + 3)

            if is_condition1_met and is_condition2_met:
                print("Solution Found:")
                print(f"Narayan's current age is: {narayan_age.value}")
                print(f"Daughter's current age is: {daughter_age.value}")
                solution_found.value = 1
                break

        if solution_found.value:
            break

    if not solution_found.value:
        print("No solution found within the specified age range.")

if __name__ == "__main__":
    main()
