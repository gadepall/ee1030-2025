import numpy as np
import time
import os


def read_pgm(f):
    p = open(f).read().split()
    p = [x for x in p if x and x[0] != '#']
    w, h, mv = int(p[1]), int(p[2]), int(p[3])
    d = np.array([int(x) for x in p[4:]], float).reshape(h, w) / mv
    return d, w, h, mv


def write_pgm(f, A, mv=255):
    h, w = A.shape
    A = np.clip(A * 255, 0, 255).astype(int)
    open(f, 'w').write(
        f'P2\n{w} {h}\n{mv}\n' +
        '\n'.join(' '.join(map(str, r)) for r in A) + '\n'
    )


f = input('Enter PGM file: ').strip()
A, w, h, mv = read_pgm(f)
nA = np.linalg.norm(A, 'fro')
ks = [1, 2, 5, 20, 50, 100, 200, 500]

print('\nk | ||A-A_k||_F | RelErr | CompRatio | Time(s)')
print('-' * 58)

for k in ks:
    t0 = time.time()
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    Ak = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    t1 = time.time()
    write_pgm(f'recon_{k}.pgm', Ak)
    e = np.linalg.norm(A - Ak, 'fro')
    r = e / nA if nA > 1e-12 else 0
    c = (h * w) / (k * (h + w + 1))
    print(f'{k:3d} | {e:10.6f} | {r:.6f} | {c:6.2f}:1 | {t1-t0:7.4f}s')
