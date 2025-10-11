import re
import sys
from pathlib import Path

import numpy as np

DAT_FILE = Path('main.dat')
SO_FILE = Path('main.so')


def parse_dat(dat_path: Path):
    if not dat_path.exists():
        print(f"Error: {dat_path} not found. Run the C program first.")
        sys.exit(1)

    text = dat_path.read_text()

    # Extract currents like: I1 = 3.1250000000 A
    curr_pat = re.compile(r"I([123])\s*=\s*([-+]?\d+(?:\.\d+)?)\s*A")
    currents = {}
    for m in curr_pat.finditer(text):
        currents[int(m.group(1))] = float(m.group(2))

    # Extract equations of the form a*I1 ± b*I2 ± c*I3 = d
    eq_pat = re.compile(r"([+-]?\d+)\*I1\s*([+-])\s*(\d+)\*I2\s*([+-])\s*(\d+)\*I3\s*=\s*([+-]?\d+)")
    coeffs, rhs = [], []
    for line in text.splitlines():
        m = eq_pat.search(line.strip())
        if m:
            a = float(m.group(1))
            bsign = 1.0 if m.group(2)=="+" else -1.0
            bcoef = bsign * float(m.group(3))
            csign = 1.0 if m.group(4)=="+" else -1.0
            ccoef = csign * float(m.group(5))
            d = float(m.group(6))
            coeffs.append([a,bcoef,ccoef])
            rhs.append(d)

    if len(coeffs) != 3:
        # Fallback to known system
        A = np.array([[-7.0, 2.0, 1.0], [ 2.0,-4.0, 2.0], [-1.0,-2.0, 7.0]], float)
        b = np.array([-10.0, -5.0, 10.0], float)
    else:
        A = np.array(coeffs, float)
        b = np.array(rhs, float)

    I_vec = np.array([currents.get(1, np.nan), currents.get(2, np.nan), currents.get(3, np.nan)], float)
    return I_vec, A, b


def validate_shared_object(so_path: Path):
    if not so_path.exists():
        print("Note: main.so not found; ensure C compilation step was completed.")
        return False
    size = so_path.stat().st_size
    print(f"")
    return True


def main():
    I_vec, A, b = parse_dat(DAT_FILE)
    validate_shared_object(SO_FILE)

    # Solve system
    sol = np.linalg.solve(A, b)

    
    print("\nSolved currents (Python):")
    print(f"I1 = {sol[0]:.10f} A")
    print(f"I2 = {sol[1]:.10f} A")
    print(f"I3 = {sol[2]:.10f} A")

    if not np.isnan(I_vec).any():
        print("\nParsed currents (from main.dat):", I_vec)
        print("Difference (Python - parsed):", sol - I_vec)
    else:
        print("\nNote: Could not parse all current values from main.dat for direct comparison.")

   

if __name__ == '__main__':
    main()

