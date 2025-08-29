import ctypes, argparse

# Load the shared object produced above
lib = ctypes.CDLL("./collinear.so")

# Configure signatures
lib.relation.argtypes = [ctypes.c_int, ctypes.c_int]
lib.relation.restype  = ctypes.c_int

lib.collinear_AO_C.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                               ctypes.POINTER(ctypes.c_double)]
lib.collinear_AO_C.restype  = ctypes.c_int

def main():
    ap = argparse.ArgumentParser(description="Check collinearity for A(1,2), O(0,0), C(a,b)")
    ap.add_argument("--a", type=float, default=3.0)
    ap.add_argument("--b", type=float, default=6.0)
    ap.add_argument("--tol", type=float, default=1e-9)
    args = ap.parse_args()

    # int API (residual = b - 2a as an int)
    r_int = lib.relation(int(round(args.a)), int(round(args.b)))

    # double API (residual + boolean)
    resid = ctypes.c_double()
    ok = lib.collinear_AO_C(args.a, args.b, args.tol, ctypes.byref(resid))

    print(f"Residual (b - 2a) via int API: {r_int}")
    print(f"Residual (b - 2a) via double API: {resid.value:.6e}")
    print("Status:", "COLLINEAR" if ok else "NOT collinear")

if __name__ == "__main__":
    main()

