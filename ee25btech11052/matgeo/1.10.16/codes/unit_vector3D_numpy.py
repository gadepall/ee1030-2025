import numpy as np

def unit_vector3d(v, tol=1e-9):
    norm = np.linalg.norm(v)
    if norm <= tol:
        raise ValueError("Zero vector cannot be normalized")
    return v / norm

if __name__ == "__main__":
    v = np.array([2, 3, 6])
    u = unit_vector3d(v)
    print("Unit vector:", u)
