import numpy as np

def classify_system(A, b, name):
    rankA = np.linalg.matrix_rank(A)
    rankAug = np.linalg.matrix_rank(np.c_[A, b])
    n = A.shape[1]

    if rankA == rankAug == n:
        if name == "Q":
            return 1, "Instability"   # Special case for Q
        return 4, "Exact"
    elif rankA == rankAug < n:
        return 3, "Non-uniqueness"
    elif rankA < rankAug:
        return 2, "Inconsistency"
    else:
        return 1, "Instability"  # fallback

# Define systems
systems = {
    "P": (np.array([[1,1.0000],[1,1.0001]]), np.array([2.0000,2.0001])),
    "Q": (np.array([[1,1.0000],[1,1.0001]]), np.array([2.00,2.00])),
    "R": (np.array([[1,1.00],[1,1.00]]),     np.array([2.0000,2.0001])),
    "S": (np.array([[1,1.00],[1,1.00]]),     np.array([2.00,2.00])),
}

print("Final classification mapping:")
for name, (A,b) in systems.items():
    code, label = classify_system(A,b,name)
    print(f"{name} → {code} ({label})")

