import numpy as np

# Define x[n] and its indices
n_x = np.array([-1, 0, 1, 2])
x = np.array([1, 1, -1, 0])

# Convolution y[n] = x[n] * x[n]
y = np.convolve(x, x)

# Indices for y[n]
n_y = np.arange(n_x[0]*2, n_x[-1]*2 + 1)
print(y)
# Value of y[-1]
t = 0 
for i in n_y :
    if i == -1 :
        ans = y[t]
        break
    t=t+1

print(f"x[n] = {x}, for n = {n_x}")
print(f"y[n] = {y}, for n = {n_y}")
print(f"y[-1] = {ans}")

